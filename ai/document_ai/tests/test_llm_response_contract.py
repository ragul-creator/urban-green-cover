"""Ensure the optional Ollama extractor uses constrained, fail-closed JSON output."""
from __future__ import annotations

from io import BytesIO
import json
from unittest.mock import patch

import pytest

from ai.document_ai.extraction.llm_extractor import OllamaEvidenceExtractor, _FIELD_RESPONSE_SCHEMA


def test_ollama_uses_constrained_schema() -> None:
    seen: dict[str, object] = {}

    def fake_urlopen(request, timeout):
        seen["body"] = json.loads(request.data.decode("utf-8"))
        seen["timeout"] = timeout
        return BytesIO(json.dumps({"response": '{"district":{"value":"Chennai","evidence":"Chennai"}}', "done_reason": "stop"}).encode("utf-8"))

    with patch("ai.document_ai.extraction.llm_extractor.urllib.request.urlopen", side_effect=fake_urlopen):
        result = OllamaEvidenceExtractor(timeout=12)._generate("Chennai")

    assert result["district"]["value"] == "Chennai"
    assert seen["body"]["format"] == _FIELD_RESPONSE_SCHEMA
    assert seen["body"]["options"]["temperature"] == 0
    assert seen["body"]["options"]["num_predict"] == 2048
    assert seen["timeout"] == 12


def test_ollama_rejects_truncated_response() -> None:
    response = BytesIO(json.dumps({"response": "{}", "done_reason": "length"}).encode("utf-8"))
    with patch("ai.document_ai.extraction.llm_extractor.urllib.request.urlopen", return_value=response):
        with pytest.raises(ValueError, match="exceeded its output limit"):
            OllamaEvidenceExtractor()._generate("sample land record")

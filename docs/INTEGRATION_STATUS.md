# Full application integration status

Updated 29 October 2026. This repository is the **full Bhumi-AI local application**, not the SIH deployment-only static demo. The original project remains preserved at `D:\12+18\intelligent-land-record-platform` on the development machine.

## Included in the application

- OCR, structured extraction, evidence-grounded optional Ollama field extraction, document validation, human review and RBAC.
- PostGIS WebGIS, imagery, building and road GeoAI, parcel candidate/delineation workflows, and SegFormer-B2 RGB+NIR land-use segmentation.
- GeoPackage inspection, private import/background processing, export, and offline synchronization API from the review-integration-hardening work.
- External GIS/LRMS/DILRMP *demo adapters*. These never connect to or certify government systems.
- Auth-session refresh locking, upload-object integrity checks, review correction normalization, GIS pagination and other integration fixes.
- Migration revisions 20260926_11/12/13 and 20261009_14 that merge interchange and existing land-use/parcel revision histories into one Alembic head.

## What was intentionally not merged

- `deploy/vercel-sih`: static demonstration screens, hardcoded viewer credentials and deployment-specific overrides. The genuine application UI remains active.
- `feature/field-landuse-segmentation` uncommitted prototype: superseded for this application's primary pipeline by the existing trained SegFormer LULC runtime. The original separate worktree and files remain untouched; it also lacks a trained benchmarked checkpoint.
- `feature/fabric-immutable-ledger` and `blockchain`: proof-of-concept ledger functions, not verified for registrar permissions, trust/governance or production networking.
- `feature/landing-page` and `urbanplan-ai`: optional branding/landing-page alternatives, not required for GIS/AI function.
- Saved evidence-only OCR demo UI was not added as a replacement for live processing.

## Validation performed

- Backend and document AI: 238 passed, 48 skipped (integration prerequisites not enabled).
- GeoAI: 85 passed using the pre-existing GPU-capable Python environment.
- Frontend: 61 passed in 10 files; production TypeScript/Vite build succeeded.
- Alembic: one head (`20261009_14`), successful offline upgrade SQL generation.
- Python `compileall`, FastAPI route import and `git diff --check` passed.
- **Not yet verified**: running the new clone against its own freshly migrated Postgres database, model-checkpoint inference from this directory, real GPU health and full upload/review end-to-end test. Passing unit tests does not certify model accuracy or statutory decisions.

## Local operation and data

Source code does not include private `.env`, database, model checkpoints, registered imagery or uploaded files. Follow the root README and provision local secrets/model mounts before starting the new clone. The original running stack and its data were not changed by this merge. The offline-sync APIs are backend support only; a complete offline field client (IndexedDB queue and service worker) is not built.

For further development use a feature branch from `main`; evaluate ledger and optional branding separately after dedicated tests.

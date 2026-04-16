# Dataset Versioning Guideline

## Goal

Dataset versions must support reproducibility, rollback, and auditability.
Teams should be able to answer what changed, why it changed, and which models consumed the change.

## Recommended Model

Use a snapshot-oriented workflow inspired by lakeFS or DVC:

1. Treat every promoted dataset as a named version.
2. Persist immutable snapshot identifiers such as commit IDs or manifest hashes.
3. Record parent-child relationships between versions.
4. Attach human-readable changelogs to every promoted snapshot.

## Minimum Required Fields

- dataset name
- semantic or date-based version
- upstream source location
- snapshot or commit ID
- owner
- validation result summary
- storage URI for the promoted artifact

## Promotion Flow

1. Ingest data into the `raw` layer.
2. Transform and validate into the `processed` layer.
3. Promote only validated outputs into the `gold` layer.
4. Assign a version and store the snapshot identifier.
5. Update all dependent experiment manifests with the promoted dataset version.

## Rollback Rule

Rollback should always target a previously validated dataset snapshot.
Never rollback by manually rewriting files in place without a new recorded version.

## Naming Guidance

Both formats below are acceptable if applied consistently:

- calendar versioning such as `2026.04.0`
- semantic versioning such as `1.3.2`

The selected version should always map to one immutable storage snapshot.

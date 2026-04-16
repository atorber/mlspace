# Data Directory Layout

## Standard Layers

### `raw/`

Stores original or source-aligned data with minimal mutation.
This layer is append-oriented and should preserve source fidelity whenever possible.

### `processed/`

Stores cleaned, normalized, and validation-ready intermediate outputs.
This layer is used for reusable transformations but should not be treated as the final training contract.

### `gold/`

Stores promoted, governed datasets approved for model training, evaluation, or serving-related downstream jobs.
Only this layer should be referenced by long-lived experiment manifests.

## Example Layout

```text
dataset_root/
  raw/
    customer_events/
      dt=2026-04-16/
  processed/
    customer_events/
      version=2026.04.0/
  gold/
    customer_events/
      version=2026.04.0/
```

## Ownership Rules

- `raw/` is typically owned by ingestion or data platform teams.
- `processed/` is jointly owned by data engineering and feature consumers.
- `gold/` must have a clearly assigned steward and promotion process.

## Operational Rules

- Do not train production models from `raw/`.
- Do not overwrite promoted data in `gold/` without creating a new version.
- Every `gold/` dataset must point back to its source and transformation lineage.

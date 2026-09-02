# Safe Human-Review Starter

## Buyer

The buyer is an operations leader who needs a visible, owned path for reviewing structured cases.

## Problem

The workflow routes a structured case without inventing an automated decision. It gives teams a safe contract to evaluate before connecting a model or external system.

## Baseline

The baseline is manual intake and review by a workflow operator. This starter does not claim to improve speed, accuracy, cost, or capacity over that baseline.

## Architecture

The caller supplies a case with `case_id` and `summary`. `process_case` validates those fields and returns a `needs_human` result. The workflow operator owns the next step. No model, database, API, or external system is connected.

## Data classification

The included input is synthetic and safe for public use. Replace it only with synthetic, public, or explicitly permitted data. Do not add secrets, customer identifiers, or private operational data.

## Evaluation

The current evaluation verifies two contract behaviors: complete cases fail closed because automation has not been evaluated, and incomplete cases name missing required fields. These tests demonstrate routing behavior only.

## Failure behavior

The workflow fails closed. Missing fields return `needs_human` with the missing field names. Complete cases also return `needs_human` until separate evidence supports a bounded automation decision.

## Human fallback

Human review is required for every result. The workflow operator owns that fallback and any final action.

## Economics claim

This starter makes no economics claim. It provides no evidence about savings, revenue, margin, payback, or production scale.

## Limitations

- No model or external system is connected.
- No production data or customer workflow has been evaluated.
- The tests do not establish decision quality or business impact.

## Quick start

From the repository root, run:

```sh
python3 -m unittest discover -s templates/workflow/tests -v
```

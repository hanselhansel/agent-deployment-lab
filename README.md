# Agent Deployment Lab

Agent Deployment Lab is a public repository for sanitized, reproducible evidence about AI-assisted business workflows. It publishes runnable contracts and synthetic examples without exposing private inputs or claiming results that have not been demonstrated.

Every workflow must pass the Defensible, Safe, Runnable, Tested, Useful, and Shareable evidence gates before public promotion. A passing starter is a contract for further evaluation, not proof of production performance.

## Start here

- [Safe human-review starter](templates/workflow/README.md)
- [Promotion checklist](PROMOTION_CHECKLIST.md)
- [Security policy](SECURITY.md)

## Verify

Run all public checks from the repository root:

```sh
python3 -m unittest tests.test_public_safety tests.test_repository_contract -v
python3 -m unittest discover -s templates/workflow/tests -v
python3 scripts/check_public_safety.py .
```

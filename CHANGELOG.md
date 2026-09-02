# Changelog

All notable changes to Agent Deployment Lab are recorded here.

## [0.1.0.0] - 2026-09-02

### Added

- Publish a fail-closed workflow starter with synthetic data, human fallback, evidence metadata, and behavior tests.
- Check public material for common credentials, private keys, and unsafe environment files before promotion.
- Define six evidence gates, public-data rules, security reporting, and MIT reuse terms.
- Run repository contracts, workflow tests, and the public safety scan in GitHub Actions.

### Changed

- Document portable test commands and ignore generated Python and local environment files.

### Fixed

- Use unittest discovery so local test modules are not shadowed by an installed package named `tests`.

# Proof of Concept README

## Introduction

- This is a starter-for-10 "proof-of-concept".
- Initial goals *very* basic:
  - Use a `yaml` file to describe a treatment pathway using small number of primitives and rules around there use.
    - Treatment Pathway to describe: [https://app.moqups.com/Gy8chXTwJkyA9TJK3t4ROyrmlb1DjxfJ/view/page/ad64222d5](https://app.moqups.com/Gy8chXTwJkyA9TJK3t4ROyrmlb1DjxfJ/view/page/ad64222d5)
  - Create a set of tests to validate the `yaml` file according to the specification of the primitives and rules.
  - ? Generate a graph from the `yaml` file and then validate that it can be traversed.

## Development

### Dependencies

- `python`:
  - Ensure `pip` is installed and updated: `python -m pip install -U pip`
  - Create `venv` for environment: e.g. `python -m venv venv`
  - Install `pytest`: `python -m pip install pytest`

- `yaml`:
  - `yaml` handling is done via the python standard library package `yaml`.

### Current state-of-affairs

- Developing from scratch (in order to write tests) a fresh treatment pathway implementation for treating diffuse large B-cell lymphoma (DLBCL)
  - See: `pathway_model.yaml`

### Notes

- Current testing environment needs to be executed from `tests` folder with `pytest`.
- The present implementation can also be executed independently, but this will be removed in due course once author is more familiar with the testing framework.

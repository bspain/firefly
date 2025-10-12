# Contributing to Firefly

Firefly is a financial independence and retirement planning toolkit. This guide explains how to get the project ready for local development and how to run the same checks that execute in CI.

## Prerequisites

- Python 3.8 or newer
- `pip`

## Install Dependencies

We recommend isolating project dependencies inside a virtual environment to avoid conflicts with global packages:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate with `.venv\Scripts\activate` instead.

Once activated, install all runtime and development requirements from the repository root:

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
```

`pip install -e .` installs Firefly in editable mode so local code changes are immediately available to your tests.

## Run Checks Locally

The CI pipeline defines three job groups. Execute the commands below from the repository root to reproduce them locally.

### 1. Unit Tests with Coverage (`test` job)

```bash
pytest tests/test_financial_calculator.py -v --cov=firefly --cov-report=term-missing --cov-report=xml --cov-fail-under=95
```

### 2. Quality Gates (`quality` job)

```bash
flake8 firefly --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 firefly --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
black --check --diff firefly tests
isort --check-only --diff firefly tests
mypy firefly --ignore-missing-imports
```

### 3. Acceptance Tests (`acceptance` job)

```bash
pytest tests/test_future_value_bdd.py -v --tb=short
```

Always run the unit tests and quality checks before the acceptance tests to mirror the CI order. All three groups must pass before opening a pull request.


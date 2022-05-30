# Poetry Sample App

A Python app using Poetry.

## Setup

[Poetry](https://python-poetry.org/) is required.

```bash
poetry install
```

## Run program

```bash
poetry run sample_py
```

## Tests

Run all tests:

```bash
poetry run pytest
```

## Coverage

```bash
poetry run pytest --cov=sample_py
```

To view an HTML report:

```bash
poetry run pytest --cov=unitconverter --cov-report html
open coverage_html_report/index.html
```

## Mypy typechecking

```bash
poetry run mypy sample_py
```

## Graph dependencies

```bash
poetry run pydeps sample_py --max-bacon=4 --cluster
```
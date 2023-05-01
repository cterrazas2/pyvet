# Running tests

## Environment

PyVet uses [Poetry](https://python-poetry.org) for management of dependencies
 and virtual environments.

Install and create a virtual environment.

```console
poetry install
```

Activate the virtual environment.

```console
poetry shell
```

All tests should pass.

```console
poetry run pytest -v
```

## Tests

To run all the tests locally, you can run:

```console
python -m unittest -v
```

or via pytest:

```console
pytest -v
```

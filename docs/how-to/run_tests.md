# Running tests

## Environment

PyVet uses [Poetry](https://python-poetry.org) for management of dependencies and virtual environments.

```console
# install and create virtual environment
$ poetry install

# activate the virtual environment
$ poetry shell

# all tests should pass
$ pytest -v
```

## Tests

To run all the tests locally, you can run:

```console
python -m unittest -v
```

or via pytest

```console
pytest -v
```

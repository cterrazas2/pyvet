# Install

## Pip

To begin using `pyvet` run the following:

```console
pip install pyvet
```

Check out the [Jupyter notebook]("https://github.com/cterrazas2/pyvet-jupyter/blob/main/explore_pyvet.ipynb")
for some examples if you just want to get up and running quickly.

## Required software for local development

* [Python](https://www.python.org/downloads/) 3.10+
* [Poetry](https://poetry.eustace.io/docs/#installation)

## Git

Clone the `pyvet` git repo.

```console
git clone git@github.com:cterrazas2/pyvet.git
```

Or use the `gh` cli:

```console
gh clone git@github.com:cterrazas2/pyvet.git
```

## Poetry

PyVet uses [Poetry](https://python-poetry.org) for management of dependencies
and virtual environments. To install the dependencies, run

```console
poetry install
```

then

```console
poetry poetry shell
```

to activate the virtual environment.

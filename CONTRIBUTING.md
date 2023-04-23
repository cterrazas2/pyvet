# Contributing to PyVet

Welcome, and thank you for wanting to contribute to `pyvet`! This is a python library that helps organizations, companies, and even veterans themselves analyze and research data from the Department of Veterans Affairs. This document outlines the quickest way to start contributing and get familiar with the code base.

# Code Setup

```
/pyvet                            # This is where the main code lives
    /benefits                     # The VA Benefits APIs
        /intake                   # The VA Benefit Intake API
            api.py                # All apis have this file
        /reference                # The VA Benefits Reference API
        ...
    /facilities                   # The VA <name> API
    .
    .
    .
    client.py                     # Where a session is created for a user (for applications that require persistence)
    creds.py                      # Where to store all credentials

/tests                            # All unit tests are here
    /benefits                     # Test the VA Benefits APIs
        test_benefits_intake.py   # Test the VA Benefits Intake API
    /data                         # Some mock data for testing
    .
    .
    .
```

# Environment

PyVet uses [Poetry](https://python-poetry.org) for management of dependencies and virtual environments.

```bash
# install and create virtual environment
$ poetry install

# activate the virtual environment
$ poetry shell

# all tests should pass
$ pytest -v
```

# Style

PyVet uses Black for code formatting, this should be automatically triggered for you when you try and commit (once you install `precommit` that is).

Check out the code base and follow the same style for things like naming conventions (snake_case) and comments (numpy).

# Tests

To run all the tests you can run:

```bash
python -m unittest -v
```

or via pytest

```bash
pytest -v
```

# Features and Bugs

Before you start working on a change, visit the [issues](https://github.com/cterrazas2/pyvet/issues) tab and see if there are any open (or closed) issues related to your change. If not, then once your change is completed locally, ideally in your own branch, ensure all tests pass (and add tests to your change), and then create a pull request filled out with all the pertinent information.

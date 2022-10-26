# PyVet
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python library to research and analyze veteran data from the Veterans Affairs (VA) Lighthouse API.

The VA Lighthouse API provides different types of veteran data through a subset of the following
apis:

-  Appeals API (internal use only)
-  Benefits API
-  Facilities API
-  Forms API
-  Health API
-  Veteran Verification API

You can find more information about these APIS and request API access [here](https://developer.va.gov/explore/).

## Install
To install the package use:
```shell
pip install pyvet
```

## Usage
To retrieve veteran data from the API, ensure your API key is set.
You should store your API key in an environment variable or in the `creds.py` named, `API_KEY`.

## VA Facilities
Here is a small example that grabs a list of all VA facilities.
```python
from pyvet.facilities.api import get_all, get_nearby

# get all VA facilities and export it to a csv file
all_facilities = get_all(print_csv_file=True)

# or just get nearby VA facilities and print a csv file
nearby_facilities = get_nearby(
    address="", # optional
    city="Boston",
    state="MA",
    zip_code="02108",
    drive_time=60,
    print_csv_file=True,
)
```
## VA Benefits Reference
```python
from pyvet.benefits_reference.api import get_disabilities, get_intake_sites

# All VA Disabilities info
disabilities = get_disabilities()

# VA Intake Sites
intake_sites = get_intake_sites()

```

## VA Forms
```python
from pyvet.forms.api import get_form, get_forms

# All VA Forms
all_forms = get_forms()

# Instructions and Enrollment Application for Health Benefits Form
form = get_form(form_name="10-10EZ")

```

## License
MIT

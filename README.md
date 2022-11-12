# PyVet
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python library to research and analyze veteran data from the [Veterans Affairs](https://github.com/department-of-veterans-affairs) (VA) Lighthouse API.

The [VA Lighthouse API](https://developer.va.gov) provides different types of veteran data through a subset of the following
apis (internal VA and Oauth token apis are not yet supported):

-  Benefits API
-  Facilities API
-  Forms API
-  Health API
-  Veteran Verification API

You can find more information about these APIS and request API access [here](https://developer.va.gov/onboarding/request-sandbox-access).

## Install
To install the package use:
```shell
pip install pyvet
```

## Usage
To retrieve veteran data from the API, ensure your API key is set.
You should store your API key in an environment variable or in the `creds.py` named, `API_KEY`.

## VA Facilities
Here is a small example that grabs a list of all, and nearby, VA facilities.
```python
from pyvet.facilities.api import get_all, get_nearby

# get all VA facilities and export it to a csv file
all_facilities = get_all(export_csv_file=True)

# or just get nearby VA facilities and export it to a csv file
nearby_facilities = get_nearby(
    address="", # optional
    city="Boston",
    state="MA",
    zip_code="02108",
    drive_time=60,
    export_csv_file=True,
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

## Veteran Confirmation
```python
from pyvet.veteran_confirmation.api import get_status

# Confirm veteran status, will return confirmed or not confirmed. Note, this is fake VA data below.
status = get_status(
    ssn="796-13-0115",
    first_name="Tamara",
    last_name="Ellis",
    birth_date="1967-06-19",
    middle_name="E",
    gender="F",
)
```

## Contributing
See the [Contributing to Pyvet](https://github.com/cterrazas2/pyvet/blob/main/CONTRIBUTING.md) documentation.

## License
MIT

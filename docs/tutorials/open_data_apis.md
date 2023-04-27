# VA Open Data APIs example requests

## Veteran Confirmation

```python
from pyvet.veteran.confirmation.api import get_status

# Confirm veteran status, will return confirmed or not confirmed. Note, this is fake VA data below.
status = get_status(
    first_name="Alfredo",
    last_name= "Armstrong",
    birth_date= "1993-06-08",
    middle_name= "M",
    gender= "M",
    street_address= "17020 Tortoise St",
    city= "Round Rock",
    zip_code= "78664",
    state= "TX",
    country= "USA",
    home_phone_number="555-555-5555",
    mothers_maiden_mame="Smith",
    birth_place_city="Johnson City",
    birth_place_state="MA",
    birth_place_country="USA",
)
```

## Veteran Benefits Intake

You can upload multiple files to the Veteran Benefits Administration (VBA) with `pyvet`.

```python
from pyvet.benefits.intake.api import create_path_to_upload_files, upload_files

params = create_path_to_upload_files()
metadata = {
    "veteranFirstName": "Jane",
    "veteranLastName": "Doe",
    "fileNumber": "012345678",
    "zipCode": "97202",
    "source": "MyVSO",
    "docType": "21-22",
    "businessLine": "CMP",
}
uploaded_files = upload_files(
    params=params,
    uploads_dir="uploads",
    metadata=metadata,
)
```

## VA Benefits Reference

```python
from pyvet.benefits.reference.api import get_disabilities, get_intake_sites

# All VA Disabilities info
disabilities = get_disabilities()

# VA Intake Sites
intake_sites = get_intake_sites()

```

## VA Facilities

Here is a small example that grabs a list of all, and nearby, VA facilities.

```python
from pyvet.facilities.api import get_all, get_nearby

# get all VA facilities and export it to a csv file
all_facilities = get_all(export_csv_file=True)

# or just get nearby VA facilities and export it to a csv file
nearby_facilities = get_nearby(
    address="", # Provide an empty string for address if unknown and then city/state/zip below to filter
    city="Boston",
    state="MA",
    zip_code="02108",
    drive_time=60, # optional
    export_csv_file=True,
)
```

## VA Forms

```python
from pyvet.forms.api import get_form, get_forms

# All VA Forms
all_forms = get_forms()

# Instructions and Enrollment Application for Health Benefits Form
form = get_form(form_name="10-10EZ")

```

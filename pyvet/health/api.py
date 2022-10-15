"""
Health API: https://developer.va.gov/explore/health
"""
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

HEALTH_URL = API_URL + "fhir/v0/"


def location(
    practitioner_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
    identifier="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
    address="151 KNOLLCROFT ROAD",
    city="LYONS",
    state="NJ",
    zip_code="07939",
    name="VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB",
    page="1",
    count=30,
):
    """Gets provider's location.
    Parameters
    ----------
    practitioner_id : str
        The id of the practitioner to locate.
    identifier : str
        The identifier of the practitioner to locate.
    address : str
        The address of the medical facility.
    city : str
        The city of the medical facility.
    state : str
        The state of the medical facility.
    zip_code : str
        The zip code of the of medical facility.
    name : str
        Name of the department within the medical facility.
    page : str
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {
        "_id": practitioner_id,
        "identifier": identifier,
        "address": address,
        "address-city": city,
        "address-state": state,
        "address-postalcode": zip_code,
        "name": name,
        "page": page,
        "_count": count,
    }
    ids_url = API_URL + "provider-directory/v0/r4" + "/Location"
    r = requests.get(ids_url, params=params, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()


def get_practitioner():
    """Get practitioner"""
    pass

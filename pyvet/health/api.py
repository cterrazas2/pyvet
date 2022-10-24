"""
Health API: https://developer.va.gov/explore/health
"""
import logging

import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session

HEALTH_URL = API_URL + "provider-directory/v0/r4/"


def get_location(
    practitioner_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
    identifier="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
    address="151 KNOLLCROFT ROAD",
    city="LYONS",
    state="NJ",
    zip_code="07939",
    name="VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB",
    page=1,
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
    page : int
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
    ids_url = HEALTH_URL + "Location"
    try:
        r = session.get(ids_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_location_by_id(resource_id: str = "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000"):
    """Gets provider's location.
    Parameters
    ----------
    resource_id: str
        The id of the practitioner to locate.
    Returns
    -------
    r : json
        Response in json format.
    """
    ids_url = HEALTH_URL + f"Location/{resource_id}"
    try:
        r = session.get(ids_url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_organization(
    org_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
    identifier="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
    address="2360 E PERSHING BLVD",
    city="CHEYENNE",
    state="WY",
    zip_code="82001",
    name="CHEYENNE VA MEDICAL",
    page=1,
    count=30,
):
    """Gets an organization's location.
    Parameters
    ----------
    org_id: str
        The id of the organization to locate.
    identifier : str
        The identifier of the organization to locate.
    address : str
        The address of the organization.
    city : str
        The city of the organization.
    state : str
        The state of the organization.
    zip_code : str
        The zip code of the organization.
    name : str
        Name of the department within the organization.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {
        "_id": org_id,
        "identifier": identifier,
        "address": address,
        "address-city": city,
        "address-state": state,
        "address-postalcode": zip_code,
        "name": name,
        "page": page,
        "_count": count,
    }
    org_url = HEALTH_URL + "Organization"
    try:
        r = session.get(org_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_organization_by_id(org_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000"):
    """Gets an organization's location.
    Parameters
    ----------
    org_id: str
        The id of the organization to locate.
    Returns
    -------
    r : json
        Response in json format.
    """
    org_url = HEALTH_URL + f"Organization/{org_id}"
    try:
        r = session.get(org_url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner(
    resource_id: str = "I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
    prac_id: str = "I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
    family: str = "DOE922",
    given: str = "JANE460",
    name: str = "DOE922",
    page: int = 1,
    count: int = 30,
):
    """Get practitioner role
    Parameters
    ----------
    resource_id: str
        The id of the resource to locate.
    prac_id: str
        The id of the practitioner role to locate.
    family: str
        The name of the practitioner role to locate.
    given: str
        The name of the practitioner role to locate.
    name: str
        The name of the practitioner role to locate.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {
        "_id": resource_id,
        "identifier": prac_id,
        "family": family,
        "given": given,
        "name": name,
        "page": page,
        "_count": count,
    }
    pr_role_url = HEALTH_URL + "Practitioner"
    try:
        r = session.get(pr_role_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_by_id(pr_id: str = "I2-HRJI2MVST2IQSPR7U5SACWIWZA000000"):
    """Get practitioner by id.
    Parameters
    ----------
    pr_id: str
        The id of the practitioner to locate.
    Returns
    -------
    r : json
        Response in json format.
    """
    pr_id_url = HEALTH_URL + f"Practitioner/{pr_id}"
    try:
        r = session.get(pr_id_url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_role(
    resource_id: str = "I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000",
    prac_id: str = "I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
    prac_name: str = "DOE922",
    page: int = 1,
    count: int = 30,
):
    """Get practitioner role
    Parameters
    ----------
    resource_id: str
        The id of the resource to locate.
    prac_id: str
        The id of the practitioner role to locate.
    prac_name: str
        The name of the practitioner role to locate.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {
        "_id": resource_id,
        "practitioner.identifier": prac_id,
        "practitioner.name": prac_name,
        "page": page,
        "_count": count,
    }
    pr_role_url = HEALTH_URL + "PractitionerRole"
    try:
        r = session.get(pr_role_url, params=params)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_role_by_id(
    pr_role_id: str = "I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000",
):
    """Get practitioner role by id.
    Parameters
    ----------
    pr_role_id: str
        The id of the practitioner role to locate.
    Returns
    -------
    r : json
        Response in json format.
    """
    pr_role_id_url = HEALTH_URL + f"PractitionerRole/{pr_role_id}"
    try:
        r = session.get(pr_role_id_url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)

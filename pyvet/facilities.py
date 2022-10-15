"""
Facilities  API: https://developer.va.gov/explore/facilities/docs/facilities?version=current
"""
import logging
import pandas as pd
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

FACILITIES_URL = API_URL + "va_facilities/v0"


def get_ids():
    """Gets all VA Facility IDs with optional params.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(type="health")
    ids_url = FACILITIES_URL + "/ids"
    retries = 0
    try:
        r = requests.get(ids_url, params=params, headers=API_KEY_HEADER)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.info(f"Connection timeout, retry #{retries}")
            get_ids()
        else:
            print(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_nearby(
    address: str = "",
    city: str = "Los Angeles",
    state: str = "CA",
    zip_code: str = "90073",
    drive_time: int = 60,
    print_csv_file: bool = False,
):
    """Gets all nearby VA Facilities with optional params.
    Parameters
    ----------
    address : str
        The address to start the search.
    city : str
        City name to start the search.
    state : str
        State to start the search.
    zip_code : str
        Zip code to start the search.
    drive_time : int
        The maximum drive time to filter results.
    print_csv_file : bool
        Flag to print the results of facilities nearby.

    Returns
    -------
    r : json
        Response in json format.
    """
    retries = 0
    params = dict(
        street_address=address,
        city=city,
        state=state,
        zip=zip_code,
        drive_time=drive_time,
    )
    nearby_url = FACILITIES_URL + "/nearby"
    try:
        r = requests.get(nearby_url, params=params, headers=API_KEY_HEADER)
        r.raise_for_status()
        r = r.json()
        if print_csv_file:
            i = 1
            output_file = "nearby.csv"
            for facility in r.get("data_json"):
                f = get_facility(facility.get("id")).get("data_json").get("attributes")
                pd_norm = pd.json_normalize(f)
                if i == 1:
                    pd_norm.to_csv(output_file)
                else:
                    pd_norm.to_csv(output_file, mode="a", header=False)
                i += 1
            logging.info(
                "Success: Nearby VA Facilities data_json populated in nearby.csv."
            )
        return r
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.error(f"Connection timeout, retry #{retries}")
            get_nearby(
                address,
                city,
                state,
                zip_code,
                drive_time,
                print_csv_file,
            )
        else:
            logging.error(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_facilities_bbox():
    """Gets all VA Facilities within a bounding box, with optional params.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(zip="92083")
    bbox_url = FACILITIES_URL + "/facilities"
    r = requests.get(bbox_url, params=params, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()


def get_all(print_csv_file: bool = False):
    """Gets all VA Facilities with optional params.
    Parameters
    ----------
    print_csv_file : bool
        Flag to print the results of facilities nearby.

    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(Accept="application/geo+json")
    all_url = FACILITIES_URL + "/facilities/all"
    retries = 0
    try:
        r = requests.get(all_url, params=params, headers=API_KEY_HEADER)
        r.raise_for_status()
        r = r.json()
        if print_csv_file:
            i = 1
            output_file = "all_va_facilities.csv"
            for facility in r.get("features"):
                pd_norm = pd.json_normalize(facility)
                if i == 1:
                    pd_norm.to_csv(output_file)
                else:
                    pd_norm.to_csv(output_file, mode="a", header=False)
                i += 1
            logging.info(
                "Success: Facilities data_json populated in all_va_facilities.csv."
            )
        return r
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.error(f"Connection timeout, retry #{retries}")
            get_all(print_csv_file)
        else:
            logging.error(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_facility(f_id: str):
    """Gets a VA Facility with required id param.
    Parameters
    ----------
    f_id : str
        Facility id to retrieve.

    Returns
    -------
    r : json
        Response in json format.
    """
    retries = 0
    params = dict(id=f_id)
    facility_url = FACILITIES_URL + "/facilities/" + f_id
    try:
        r = requests.get(facility_url, params=params, headers=API_KEY_HEADER)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.error(f"Connection timeout, retry #{retries}")
            get_facility(f_id)
        else:
            logging.error(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)

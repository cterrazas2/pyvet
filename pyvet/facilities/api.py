"""
Facilities  API: https://developer.va.gov/explore/facilities/docs/facilities?version=current
"""
# mypy: disable-error-code="attr-defined"
import logging

import pandas as pd

from pyvet.client import current_session as session
from pyvet.client import session_call
from pyvet.creds import API_URL
from pyvet.json_alias import Json

FACILITIES_URL = API_URL + "va_facilities/v0"
FACILITIES_QUERY_MSG = """
    Parameter combinations for `/facilities` query not met:

    You may optionally specify page and per_page with any query. You must specify one of the following parameter combinations:
    bbox[], with the option of any combination of type, services[], or mobile
    ids
    lat and long, with the option of any combination of radius, ids, type, services[], or mobile
    state, with the option of any combination of type, services[], or mobile
    visn
    zip, with the option of any combination of type, services[], or mobile
    """


def export_to_csv(file_name: str, data: list[dict[str, str]]) -> None:
    """Exports data to csv file.
    Parameters
    ----------
    file_name : str
        The name of the csv file.
    data : list
        The data to be exported.
    """
    for i, row in enumerate(data):
        pd_norm = pd.json_normalize(row)
        if i == 0:
            pd_norm.to_csv(file_name)
        else:
            pd_norm.to_csv(file_name, mode="a", header=False)


@session_call()
def get_ids() -> Json:
    """Gets all VA Facility IDs with optional params.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {"type": "health"}
    ids_url = FACILITIES_URL + "/ids"
    return session.get(ids_url, params=params)


@session_call()
def get_nearby(
    latitude: float,
    longitude: float,
    drive_time: int | None = None,
    export_csv_file: bool = False,
) -> Json:
    """Gets all VA Facilities within a certain drive time.
    Parameters
    ----------
    latitude : float
        The latitude to search.
    longitude : float
        The longitude to search.
    drive_time : int
        The drive time to search.
    export_csv_file : bool
        Whether to export data to csv file.
    Returns
    -------
    json_conversion : json
        Response in json format.
    """
    params = {
        "lat": latitude,
        "lng": longitude,
        "drive_time": drive_time,
    }
    nearby_url = FACILITIES_URL + "/nearby"
    response = session.get(nearby_url, params=params)
    if export_csv_file:
        output_file = "nearby.csv"
        csv_data = response.get("data")
        export_to_csv(file_name=output_file, data=csv_data)
        logging.info("Success: Nearby VA Facilities data populated in %s.", output_file)
    return response


@session_call()
def get_facilities_by_query(
    bbox: list[float] | None = None,
    ids: list[str] | None = None,
    latitude: float | None = None,
    longitude: float | None = None,
    radius: float | None = None,
    facility_type: str | None = None,
    services: list[str] | None = None,
    mobile: bool | None = None,
    state: str | None = None,
    visn: int | None = None,
    zip_code: str | None = None,
    page: int = 1,
    per_page: int = 30,
) -> Json:
    """Gets all VA Facilities with optional params.
    Parameters
    ----------
    bbox : list
        The bounding box to search.
    ids : list
        The ids to search.
    latitude : float
        The latitude to search.
    longitude : float
        The longitude to search.
    radius : float
        The radius to search.
    facility_type : str
        The facility type to search ["health", "benefits", "cemetery", "vet_center"].
    services : list
        The services to search.
    mobile : bool
        The mobile to search.
    state : str
        The state to search.
    visn : int
        The visn to search.
    zip_code : str
        The zip code to search.
    page : int
        The page to search.
    per_page : int
        The per page to search.
    Returns
    -------
    r : json
        Response in json format.
    """
    # See FACILITIES_QUERY_MSG above for VA requirement here
    combos_met = (
        (
            ids
            and not bbox
            and not latitude
            and not longitude
            and not radius
            and not state
            and not visn
            and not zip_code
        )
        or (
            (latitude and longitude)
            and not bbox
            and not state
            and not visn
            and not zip_code
        )
        or (
            bbox
            and not latitude
            and not longitude
            and not radius
            and not state
            and not visn
            and not zip_code
        )
        or (
            state
            and not bbox
            and not latitude
            and not longitude
            and not radius
            and not visn
            and not zip_code
        )
        or (
            zip_code
            and not bbox
            and not latitude
            and not longitude
            and not radius
            and not state
            and not visn
        )
        or (
            visn
            and not bbox
            and not latitude
            and not longitude
            and not radius
            and not state
            and not facility_type
            and not zip_code
        )
    )
    if combos_met:
        params = {
            "bbox": bbox,
            "ids": ids,
            "lat": latitude,
            "long": longitude,
            "radius": radius,
            "type": facility_type,
            "services": services,
            "mobile": mobile,
            "state": state,
            "visn": visn,
            "zip": zip_code,
            "page": page,
            "per_page": per_page,
        }
        bbox_url = FACILITIES_URL + "/facilities"
        return session.get(bbox_url, params=params)
    logging.error(FACILITIES_QUERY_MSG)


@session_call()
def get_all(export_csv_file: bool = False) -> Json:
    """Gets all VA Facilities.
    Parameters
    ----------
    export_csv_file : bool
        Whether to export data to csv file.
    Returns
    -------
    json_conversion : json
        Response in json format.
    """
    params = {"Accept": "application/geo+json"}
    all_url = FACILITIES_URL + "/facilities/all"
    response = session.get(all_url, params=params)
    if export_csv_file:
        output_file = "all_va_facilities.csv"
        csv_data = response.get("features")
        export_to_csv(file_name=output_file, data=csv_data)
        logging.info("Success: Facilities data populated in %s.", output_file)
    return response


@session_call()
def get_facility(f_id: str) -> Json:
    """Gets a VA Facility by id.
    Parameters
    ----------
    f_id : str
        The id of the facility.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = {"id": f_id}
    facility_url = FACILITIES_URL + "/facilities/" + f_id
    return session.get(
        facility_url,
        params=params,
    )

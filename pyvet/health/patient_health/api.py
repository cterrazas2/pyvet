"""
Health API: https://developer.va.gov/explore/health/docs/fhir?version=current

Resources

    Organization
    Patient
    Practitioner
    PractitionerRole
    Procedure
    Metadata
"""
import logging

import requests

from pyvet.creds import API_URL
from pyvet.client import (
    current_session as session,
    get_bearer_token,
)
from typing import List

HEALTH_URL = API_URL + "fhir/v0/r4/"
HEALTH_SCOPE = "profile openid offline_access launch/patient patient/AllergyIntolerance.read patient/Appointment.read patient/Binary.read patient/Condition.read patient/Device.read patient/DeviceRequest.read patient/DiagnosticReport.read patient/DocumentReference.read patient/Encounter.read patient/Immunization.read patient/Location.read patient/Medication.read patient/MedicationOrder.read patient/MedicationRequest.read patient/MedicationStatement.read patient/Observation.read patient/Organization.read patient/Patient.read patient/Practitioner.read patient/PractitionerRole.read patient/Procedure.read"


def get_allergy_intolerance(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets allergy intolerance.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    last_updated : str
        The last updated date of the resource.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    allergy_url = HEALTH_URL + "AllergyIntolerance"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(allergy_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_allergy_intolerance_by_id(resource_id: str):
    """Gets allergy intolerance by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    allergy_url = HEALTH_URL + f"AllergyIntolerance/{resource_id}"
    try:
        r = session.get(allergy_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_appointment(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    location: str = None,
    last_updated: List[str] = None,
    date: List[str] = None,
    page: int = 1,
    count: int = 30,
):
    """Gets appointment.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    location : str
        The location of the appointment.
    last_updated : List[str]
        The list of date(s) of when the appointment was last updated.
    date : List[str]
        The list of date(s) of the appointment.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    appointment_url = HEALTH_URL + "Appointment"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "location": location,
        "_lastUpdated": last_updated,
        "date": date,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(appointment_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_appointment_by_id(resource_id: str):
    """Gets appointment by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    appointment_url = HEALTH_URL + f"Appointment/{resource_id}"
    try:
        r = session.get(appointment_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_binary_by_id(resource_id: str):
    """Gets binary by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    binary_url = HEALTH_URL + f"Binary/{resource_id}"
    try:
        r = session.get(binary_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_condition(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    category: str = None,
    clinical_status: str = None,
    code: str = None,
    onset_date: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets condition.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    category : str
        The category of the condition.
    clinical_status : str
        The clinical status of the condition.
    code : str
        The code of the condition.
    onset_date : str
        The date of onset of the condition.
    last_updated : str
        The dat of when the comdition record was last updated.
    date : List[str]
        The list of date(s) of the appointment.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    condition_url = HEALTH_URL + "Condition"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "category": category,
        "clinical-status": clinical_status,
        "code": code,
        "onset-date": onset_date,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(condition_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_condition_by_id(resource_id: str):
    """Gets condition by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    condition_url = HEALTH_URL + f"Condition/{resource_id}"
    try:
        r = session.get(condition_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_device(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    type: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets device.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    type : str
        The code used to identify the medical device.
    last_updated : str
        The date of when the device record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    condition_url = HEALTH_URL + "Device"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "type": type,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(condition_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_device_by_id(resource_id: str):
    """Gets device by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    device_url = HEALTH_URL + f"Device/{resource_id}"
    try:
        r = session.get(device_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_device_request(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets device request.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    last_updated : str
        The date of when the device request record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    device_request_url = HEALTH_URL + "DeviceRequest"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(device_request_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_device_request_by_id(resource_id: str):
    """Gets device request by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    device_request_url = HEALTH_URL + f"DeviceRequest/{resource_id}"
    try:
        r = session.get(device_request_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_diagnostic_report(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    category: str = None,
    code: str = None,
    date: List[str] = None,
    status: str = None,
    last_updated: List[str] = None,
    page: int = 1,
    count: int = 30,
):
    """Gets diagnostic report.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    category : str
        The category of the diagnostic report.
    code : str
        The code of the diagnostic report.
    date : List[str]
        The list of date(s) of the diagnostic report.
    status : str
        The status of the diagnostic report.
    last_updated : List[str]
        The list of date(s) of when the diagnostic report was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    diagnostic_report_url = HEALTH_URL + "DiagnosticReport"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "category": category,
        "code": code,
        "date": date,
        "status": status,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(diagnostic_report_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_diagnostic_report_by_id(resource_id: str):
    """Gets diagnostic report by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    diagnostic_report_url = HEALTH_URL + f"DiagnosticReport/{resource_id}"
    try:
        r = session.get(diagnostic_report_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_document_reference(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    type: str = None,
    date: List[str] = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets document reference.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    type : str
        The type of the document reference.
    date : List[str]
        The list of date(s) of the document reference.
    last_updated : str
        The date of when the document reference record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    document_reference_url = HEALTH_URL + "DocumentReference"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "type": type,
        "date": date,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(document_reference_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_document_reference_by_id(resource_id: str):
    """Gets document reference by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    document_reference_url = HEALTH_URL + f"DocumentReference/{resource_id}"
    try:
        r = session.get(document_reference_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_encounter(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    date: List[str] = None,
    last_updated: List[str] = None,
    page: int = 1,
    count: int = 30,
):
    """Gets encounter.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    date : List[str]
        The list of date(s) of the encounter.
    last_updated : List[str]
        The list of date(s) of when the encounter was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    encounter_url = HEALTH_URL + "Encounter"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "date": date,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(encounter_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_encounter_by_id(resource_id: str):
    """Gets encounter by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    encounter_url = HEALTH_URL + f"Encounter/{resource_id}"
    try:
        r = session.get(encounter_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_immunization(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets immunization.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    last_updated : str
        The date of when the immunization record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    immunization_url = HEALTH_URL + "Immunization"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(immunization_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_immunization_by_id(resource_id: str):
    """Gets immunization by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    immunization_url = HEALTH_URL + f"Immunization/{resource_id}"
    try:
        r = session.get(immunization_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_location(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    address_city: str = None,
    address_state: str = None,
    address_postal_code: str = None,
    name: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets location.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    address_city : str
        The city of the location.
    address_state : str
        The state of the location.
    address_postal_code : str
        The postal code of the location.
    name : str
        The name of the location.
    last_updated : str
        The date of when the location record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    location_url = HEALTH_URL + "Location"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "address-city": address_city,
        "address-state": address_state,
        "address-postal-code": address_postal_code,
        "name": name,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(location_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_location_by_id(resource_id: str):
    """Gets immunization by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    location_url = HEALTH_URL + f"Location/{resource_id}"
    try:
        r = session.get(location_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_medication(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets medication.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    last_updated : str
        The date of when the medication record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    medication_url = HEALTH_URL + "Medication"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(medication_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_medication_by_id(resource_id: str):
    """Gets medication by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    medication_url = HEALTH_URL + f"Medication/{resource_id}"
    try:
        r = session.get(medication_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_medication_request(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    last_updated: str = None,
    intent: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets medication request.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    last_updated : str
        The date of when the medication request record was last updated.
    intent : str
        The intent of the medication request.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    medication_request_url = HEALTH_URL + "MedicationRequest"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "_lastUpdated": last_updated,
        "intent": intent,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(medication_request_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_medication_request_by_id(resource_id: str):
    """Gets medication request by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    medication_request_url = HEALTH_URL + f"MedicationRequest/{resource_id}"
    try:
        r = session.get(medication_request_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_observation(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    category: str = None,
    code: str = None,
    date: List[str] = None,
    last_updated: List[str] = None,
    page: int = 1,
    count: int = 30,
):
    """Gets observation.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    category : str
        The category of the observation.
    code : str
        The code of the observation.
    date : List[str]
        The list of date(s) of the observation.
    last_updated : List[str]
        The list of date(s) of when the observation was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    observation_url = HEALTH_URL + "Observation"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "category": category,
        "code": code,
        "date": date,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(observation_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_observation_by_id(resource_id: str):
    """Gets observation by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    observation_url = HEALTH_URL + f"Observation/{resource_id}"
    try:
        r = session.get(observation_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_organization(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    address_city: str = None,
    address_state: str = None,
    address_postal_code: str = None,
    name: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets organization.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    address_city : str
        The city of the organization.
    address_state : str
        The state of the organization.
    address_postal_code : str
        The postal code of the organization.
    name : str
        The name of the organization.
    last_updated : str
        The date of when the organization record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    organization_url = HEALTH_URL + "Organization"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "address-city": address_city,
        "address-state": address_state,
        "address-postal-code": address_postal_code,
        "name": name,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(organization_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_organization_by_id(resource_id: str):
    """Gets organization by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    organization_url = HEALTH_URL + f"Organization/{resource_id}"
    try:
        r = session.get(organization_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_patient(
    resource_id: str = None,
    identifier: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets patient.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    patient_url = HEALTH_URL + "Patient"
    params = {
        "_id": resource_id,
        "identifier": identifier,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(patient_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_patient_by_id(resource_id: str):
    """Gets patient by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    patient_url = HEALTH_URL + f"Patient{resource_id}"
    try:
        r = session.get(patient_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner(
    resource_id: str = None,
    identifier: str = None,
    family: str = None,
    given: str = None,
    name: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets practitioner.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    family : str
        The family name of the practitioner.
    given : str
        The given name of the practitioner.
    name : str
        The given or family name of the practitioner.
    last_updated : str
        The date of when the practitioner record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    practitioner_url = HEALTH_URL + "Practitioner"
    params = {
        "_id": resource_id,
        "identifier": identifier,
        "family": family,
        "given": given,
        "name": name,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(practitioner_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_by_id(resource_id: str):
    """Gets practitioner by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    practitioner_url = HEALTH_URL + f"Practitioner/{resource_id}"
    try:
        r = session.get(practitioner_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_role(
    resource_id: str = None,
    identifier: str = None,
    name: str = None,
    last_updated: str = None,
    page: int = 1,
    count: int = 30,
):
    """Gets practitioner role.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    name : str
        The name of the practitioner role.
    last_updated : str
        The date of when the practitioner role record was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    practitioner_role_url = HEALTH_URL + "PractitionerRole"
    params = {
        "_id": resource_id,
        "identifier": identifier,
        "name": name,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(practitioner_role_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_practitioner_role_by_id(resource_id: str):
    """Gets practitioner role by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    practitioner_role_url = HEALTH_URL + f"PractitionerRole/{resource_id}"
    try:
        r = session.get(practitioner_role_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_procedure(
    patient: str = None,
    resource_id: str = None,
    identifier: str = None,
    date: List[str] = None,
    last_updated: List[str] = None,
    page: int = 1,
    count: int = 30,
):
    """Gets procedure.
    Parameters
    ----------
    patient : str
        The patient's icn.
    resource_id : str
        The logical id of the resource.
    identifier : str
        The logical identifier of the resource.
    date : List[str]
        The list of date(s) that describes the date that the procedure was performed.
    last_updated : List[str]
        The list of date(s) of when the procedure was last updated.
    page : int
        The number of pages to limit.
    count : int
        Maximum count to limit.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    procedure_url = HEALTH_URL + "Procedure"
    params = {
        "patient": patient,
        "_id": resource_id,
        "identifier": identifier,
        "date": date,
        "_lastUpdated": last_updated,
        "page": page,
        "_count": count,
    }
    try:
        r = session.get(procedure_url, headers=session.headers, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_procedure_by_id(resource_id: str):
    """Gets procedure by id.
    Parameters
    ----------
    resource_id : str
        The logical id of the resource.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    procedure_url = HEALTH_URL + f"Procedure/{resource_id}"
    try:
        r = session.get(procedure_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_metadata():
    """Gets metadata.
    Returns
    -------
    r : json
        Response in json format.
    """
    if session.headers.get("Authorization") is None:
        token = get_bearer_token(va_api="fhir", scope=HEALTH_SCOPE)
        if token is None:
            logging.error("Fetching token failed.")
            return
        session.headers["Authorization"] = f"Bearer {token}"
    metadata_url = HEALTH_URL + "metadata"
    try:
        r = session.get(metadata_url, headers=session.headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)
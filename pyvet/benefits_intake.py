"""
Benefits Intake API: https://developer.va.gov/explore/benefits/docs/benefits?version=current
"""
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

BENEFITS_INTAKE_URL = API_URL + "vba_documents/v1/"


def create_path_and_upload_file():
    """Creates a path and then uploads a file.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + "uploads"
    r = requests.post(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    r = r.json()
    print(f"request = {r}")
    attrs = r.get("data_json").get("attributes")
    params = {**attrs}
    upload_file(params=params)
    return r.json()


def upload_file(params):
    """Upload a file for benefit intake.
    Parameters
    ----------
    params : dict
        The params to submit with the file upload.

    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + "path"
    print(f"params = {params}")
    r = requests.put(ref_url, data=params, headers=API_KEY_HEADER)
    print(f"upload_file request = {r}")
    r.raise_for_status()
    return r.json()


def bulk_status_report():
    """Retrieves a bulk status report of all reports uploaded.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + "uploads/report"
    r = requests.post(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()


def get_uploaded_document(doc_id):
    """Get an uploaded document.
    Parameters
    ----------
    doc_id : str
        The doc id to fetch.

    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + f"uploads/{doc_id}"
    r = requests.get(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()


def download_uploaded_document(doc_id):
    """Downloads a previously uploaded document.
    Parameters
    ----------
    doc_id : str
        The doc id of the document to download.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + f"uploads/{doc_id}/download"
    r = requests.get(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()

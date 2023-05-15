"""
Benefits Intake API: https://developer.va.gov/explore/benefits/docs/benefits?version=current
"""
# mypy: disable-error-code="attr-defined"
import json
import logging
import os
import pathlib

import requests

from pyvet.client import current_session as session
from pyvet.client import session_call
from pyvet.creds import API_URL
from pyvet.json_alias import Json

BENEFITS_INTAKE_URL = API_URL + "vba_documents/v1/"


@session_call()
def create_path_to_upload_files() -> Json:
    """Creates a path to upload files to the VA benefits intake api.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + "uploads"
    response = session.post(ref_url)
    return response.get("data").get("attributes")


@session_call(exceptions=(requests.exceptions.RequestException, OSError))
def upload_files(
    params: dict[str, str],
    uploads_dir: str = "uploads",
    metadata: dict[str, str] | None = None,
) -> requests.Response | None:
    """Uploads file(s) to the benefit intake api.
    Parameters
    ----------
    params : dict
        The params to extract the location to submit the file upload.
    uploads_dir: str
        The name of the directory for file uploads.
    metadata: dict
        A dict with optional file metadata.

    Returns
    -------
    r : Response
        A Response object from requests.

    Notes
    -------
    To upload files to the VA benefits intake api, files must contain any of
    the below fields (except metadata) and all naming must match exactly:
        metadata - a dict of file metadata
        content - main content file
        attachment1 - 1st attachment file
        attachmentN - Nth attachment file

    Currently, pyvet will look in the uploads_dir, defaults to `uploads/`,
    within the current working directory. You should ensure this directory
    exists and place all files you want to upload here. Below is an example
    file structure:

    uploads/
        attachments/
            attachment1.pdf
            attachment2.pdf
        main_content.pdf

    """

    uploads_dir = pathlib.Path().resolve().as_posix() + f"/{uploads_dir}/"
    attachments_dir = uploads_dir + "attachments/"

    files: dict = {}

    # add any metadata
    if metadata:
        try:
            serialized_json = json.dumps(metadata)
            files["metadata"] = (None, f"{serialized_json};type=application/json")
        except TypeError as e:
            logging.error(e)
    # upload the main content pdf
    for file in os.listdir(uploads_dir):
        if not os.path.isdir(file) and "attachments" not in file:
            with open(uploads_dir + file, "rb") as f:
                files["content"] = f.read()

    # then upload all other attachment pdfs
    for i, file in enumerate(os.listdir(attachments_dir)):
        with open(attachments_dir + file, "rb") as f:
            files[f"attachment{i+1}"] = f.read()

    file_url: str | bytes = params.get("location", "")
    if not file_url:
        logging.error("No file upload location found.")
        return None

    return session.put(
        url=file_url,
        files=files,
    )


@session_call()
def bulk_status_report(guids: list[str]) -> Json:
    """Get the status of multiple documents.
    Parameters
    ----------
    guids : list
        A list of guids to fetch the status of.

    Returns
    -------
    r : json
        Response in json format.
    """
    status_url = BENEFITS_INTAKE_URL + "uploads/report"
    return session.post(status_url, json={"ids": guids})


@session_call()
def get_uploaded_document(doc_id: str) -> Json:
    """Gets the status of a previously uploaded document.
    Parameters
    ----------
    doc_id : str
        The doc id of the document to get the status of.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = BENEFITS_INTAKE_URL + f"uploads/{doc_id}"
    return session.get(ref_url)


@session_call()
def download_uploaded_document(doc_id: str) -> Json:
    """Downloads a previously uploaded document. This endpoint is only for testing environment.
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
    return session.get(ref_url)

"""
Benefits Intake API: https://developer.va.gov/explore/benefits/docs/claims?version=v1
Note: V1 is for external users, V2 is for internal users.
"""
import logging

import requests

from pyvet.client import (
    current_session as session,
)
from pyvet.client import (
    get_bearer_token,
)
from pyvet.creds import API_URL
from pyvet.json_alias import Json

BENEFITS_INTAKE_URL = API_URL + "claims/v1/"
CLAIM_SCOPE = "openid profile offline_access claim.read claim.write"


def get_claims(
    is_representative: bool = False,
    ssn: str = "",
    first_name: str = "",
    last_name: str = "",
    birth_date: str = "",
) -> Json:
    """Get claims for a veteran.
    Parameters
    ----------
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    claims_url = BENEFITS_INTAKE_URL + "claims"
    authorization = session.headers.get("Authorization")
    if authorization is None:
        logging.error("No token set.")
        session.headers[
            "Authorization"
        ] = f"""Bearer {get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        logging.error("Fetching token failed.")
        return None
    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date
    try:
        r = session.get(claims_url, headers=session.headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_claim(
    claim_id: str,
    is_representative: bool = False,
    ssn: str = "",
    first_name: str = "",
    last_name: str = "",
    birth_date: str = "",
):
    """Get claim details.
    Parameters
    ----------
    claim_id : str
        The claim id.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    claim_url = BENEFITS_INTAKE_URL + f"claims/{claim_id}"
    authorization = session.headers.get("Authorization")
    if authorization is None:
        logging.error("No token set.")
        session.headers[
            "Authorization"
        ] = f"""Bearer {get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        logging.error("Fetching token failed.")
        return None
    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date
    try:
        r = session.get(claim_url, headers=session.headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def submit_526(
    is_first_claim: bool = False,
    is_representative: bool = False,
    ssn: str = "",
    first_name: str = "",
    last_name: str = "",
    birth_date: str = "",
) -> Json:
    """Submit a 526 claim.
    Parameters
    ----------
    is_first_claim : bool
        If this is the veteran's first claim.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    submission_url = BENEFITS_INTAKE_URL + "forms/526"
    token = get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)
    if session.headers.get("Authorization") is None:
        session.headers["Authorization"] = f"Bearer {token}"

    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date

    try:
        with open("form526.pdf", "rb") as f:
            form_256 = f.read()
        r = session.post(
            submission_url,
            headers=session.headers,
            files=form_256 if is_first_claim else None,  # type: ignore[arg-type]
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


# def upload_526(
#     doc_id: str,
#     is_representative: bool = False,
#     ssn: str = "",
#     first_name: str = "",
#     last_name: str = "",
#     birth_date: str = "",
# ) -> Json:
#     """Upload a 526 claim.
#     Parameters
#     ----------
#     doc_id : str
#         The document id.
#     is_representative : bool
#         If the consumer is a representative on behalf of a veteran.
#     ssn : str
#         The veteran's SSN.
#     first_name : str
#         The veteran's first name.
#     last_name : str
#         The veteran's last name.
#     birth_date : str
#         The veteran's birth date in iso8601 format.
#     Returns
#     -------
#     r : json
#         Response in json format.
#     """
#     pass


# def upload_supporting_doc_526(
#     doc_id: str,
#     is_representative: bool = False,
#     ssn: str = "",
#     first_name: str = "",
#     last_name: str = "",
#     birth_date: str = "",
# ):
#     """Upload a supporting document for a 526 claim.
#     Parameters
#     ----------
#     doc_id : str
#         The document id.
#     is_representative : bool
#         If the consumer is a representative on behalf of a veteran.
#     ssn : str
#         The veteran's SSN.
#     first_name : str
#         The veteran's first name.
#     last_name : str
#         The veteran's last name.
#     birth_date : str
#         The veteran's birth date in iso8601 format.
#     Returns
#     -------
#     r : json
#         Response in json format.
#     """
#     pass


# def submit_intent_to_file(
#     is_representative: bool = False,
#     ssn: str = "",
#     first_name: str = "",
#     last_name: str = "",
#     birth_date: str = "",
# ) -> Json:
#     """Submit an intent to file for disability compensation, burial, or pension claims.
#     is_representative : bool
#         If the consumer is a representative on behalf of a veteran.
#     ssn : str
#         The veteran's SSN.
#     first_name : str
#         The veteran's first name.
#     last_name : str
#         The veteran's last name.
#     birth_date : str
#         The veteran's birth date in iso8601 format.
#     Returns
#     -------
#     r : json
#         Response in json format.
#     """
#     pass


def get_last_active_intent_to_file(
    is_representative: bool = False,
    intent_type: str = "compensation",
    ssn: str = "",
    first_name: str = "",
    last_name: str = "",
    birth_date: str = "",
) -> Json:
    """Get the last active intent to file for disability compensation, burial, or pension claims.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    active_intent_url = BENEFITS_INTAKE_URL + "forms/0966/active"
    authorization = session.headers.get("Authorization")
    if authorization is None:
        logging.error("No token set.")
        session.headers[
            "Authorization"
        ] = f"""Bearer {get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        logging.error("Fetching token failed.")
        return None
    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date
    try:
        r = session.get(
            active_intent_url, headers=session.headers, params={"type": intent_type}
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


# def submit_poa(
#     is_representative: bool = False,
#     ssn: str = "",
#     first_name: str = "",
#     last_name: str = "",
#     birth_date: str = "",
# ) -> Json:
#     """Submit a Power of Attorney form 2122.
#     Parameters
#     ----------
#     is_representative : bool
#         If the consumer is a representative on behalf of a veteran.
#     ssn : str
#         The veteran's SSN.
#     first_name : str
#         The veteran's first name.
#     last_name : str
#         The veteran's last name.
#     birth_date : str
#         The veteran's birth date in iso8601 format.
#     Returns
#     -------
#     r : json
#         Response in json format.
#     """
#     pass


# def upload_signed_poa(
#     poa_id: str,
#     is_representative: bool = False,
#     ssn: str = "",
#     first_name: str = "",
#     last_name: str = "",
#     birth_date: str = "",
# ) -> Json:
#     """Upload a signed Power of Attorney form 2122.
#     Parameters
#     ----------
#     poa_id : str
#         The id of the Power of Attorney form 2122.
#     is_representative : bool
#         If the consumer is a representative on behalf of a veteran.
#     ssn : str
#         The veteran's SSN.
#     first_name : str
#         The veteran's first name.
#     last_name : str
#         The veteran's last name.
#     birth_date : str
#         The veteran's birth date in iso8601 format.
#     Returns
#     -------
#     r : json
#         Response in json format.
#     """
#     pass


def get_poa_status_by_id(
    poa_id: str,
    is_representative: bool = False,
    ssn: str = "",
    first_name: str = "",
    last_name: str = "",
    birth_date: str = "",
) -> Json:
    """Get the status of a Power of Attorney form 2122 by an id.
    Parameters
    ----------
    poa_id : str
        The id of the Power of Attorney form 2122.
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    poa_url = BENEFITS_INTAKE_URL + f"forms/2122/{poa_id}"
    authorization = session.headers.get("Authorization")
    if authorization is None:
        logging.error("No token set.")
        session.headers[
            "Authorization"
        ] = f"""Bearer {get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        logging.error("Fetching token failed.")
        return None
    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date
    try:
        r = session.get(poa_url, headers=session.headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_status_poa_last_active(
    is_representative: bool = False,
    ssn: str = "",
    first_name: str = "",
    last_name: str = "",
    birth_date: str = "",
) -> Json:
    """Get the status of the last active Power of Attorney form 2122.
    Parameters
    ----------
    is_representative : bool
        If the consumer is a representative on behalf of a veteran.
    ssn : str
        The veteran's SSN.
    first_name : str
        The veteran's first name.
    last_name : str
        The veteran's last name.
    birth_date : str
        The veteran's birth date in iso8601 format.
    Returns
    -------
    r : json
        Response in json format.
    """
    poa_url = BENEFITS_INTAKE_URL + "forms/2122/active"
    authorization = session.headers.get("Authorization")
    if authorization is None:
        logging.error("No token set.")
        session.headers[
            "Authorization"
        ] = f"""Bearer {get_bearer_token(va_api="claims", scope=CLAIM_SCOPE)}"""
    if session.headers.get("Authorization") is None:
        logging.error("Fetching token failed.")
        return None
    if is_representative:
        session.headers["X-VA-SSN"] = ssn
        session.headers["X-VA-First-Name"] = first_name
        session.headers["X-VA-Last-Name"] = last_name
        session.headers["X-VA-Birth-Date"] = birth_date
    try:
        r = session.get(poa_url, headers=session.headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(e)

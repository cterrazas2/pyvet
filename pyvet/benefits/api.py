"""
Benefits API: https://developer.va.gov/explore/benefits/docs/claims?version=current
"""
import logging
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

CLAIMS_URL = API_URL + "claims/v1"


def get_claims(ssn: str, fn: str, ln: str):
    """
    Parameters
    ----------
    ssn : str
        Veteran's ssn to submit for claims.
    fn : str
        First name of veteran.
    ln : str
        Last name of veteran.

    Returns
    -------

    """
    payload = {"X-VA-SSN": ssn, "X-VA-First-Name": fn, "X-VA-Last-Name": ln}
    claims_url = CLAIMS_URL + "/claims"
    return requests.get(claims_url, params=payload)


def get_claim(claim_id: str, ssn: str = "", fn: str = "", ln: str = ""):
    """Gets a claim for a veteran by an id, with required params.
    Parameters
    ----------
    claim_id : str
        I for claim.
    ssn : str
        Veteran's ssn for claim.
    fn : str
        Veteran's first name.
    ln : str
        Veteran's last name.
    Returns
    -------
    """
    retries = 0
    claim_url = CLAIMS_URL + "/claims/" + claim_id
    claim_headers = dict(**API_KEY_HEADER)
    claim_headers["id"] = claim_id
    claim_headers["X-VA-SSN"] = ssn
    claim_headers["X-VA-First-Name"] = fn
    claim_headers["X-VA-Last-Name"] = ln
    try:
        r = requests.get(claim_url, headers=claim_headers)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.error(f"Connection timeout, retry #{retries}")
            get_claim(claim_id, ssn, fn, ln)
        else:
            logging.error(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)


def submit_claim(ssn: str, fn: str, ln: str, bd: str):
    """Submits a claim for a veteran with required params.
    Parameters
    ----------
    ssn : str
        Veteran's ssn for claim.
    fn : str
        Veteran's first name.
    ln : str
        Veteran's last name.
    bd : str
        Veteran's birthdate.
    Returns
    -------

    """
    payload = {
        "X-VA-SSN": ssn,
        "X-VA-First-Name": fn,
        "X-VA-Last-Name": ln,
        "X-VA-Birth-Date": bd,
    }
    data = {
        "type": "form/526",
        "attributes": {"veteran": {"currentlyVAEmployee": "false"}},
    }
    claim_url = CLAIMS_URL + "/forms/526"
    return requests.post(claim_url, params=payload, data=data)


def upload_to_claim(claim_id: str, ssn: str, fn: str, ln: str, bd: str):
    """Uploads data_json to a veteran's claim by a claim id, with required params.
    Parameters
    ----------
    claim_id : str
        ID of claim.
    ssn : str
        Veteran's ssn for claim.
    fn : str
        Veteran's first name.
    ln : str
        Veteran's last name.
    bd : str
        Veteran's birthdate.

    Returns
    -------

    """
    payload = {
        "id": claim_id,
        "X-VA-SSN": ssn,
        "X-VA-First-Name": fn,
        "X-VA-Last-Name": ln,
        "X-VA-Birth-Date": bd,
    }
    data = {"data_json": {"id": claim_id, "type": "claims_api_claim", "attributes": {}}}
    claim_url = CLAIMS_URL + "/forms/526/"
    return requests.put(claim_url, params=payload, data=data)


def get_disabilities():
    """Returns all VA disabilities.
    Returns
    -------
    r : json
        Response in json format.
    """
    ref_url = API_URL + "benefits-reference-data_json/v1/disabilities"
    r = requests.get(ref_url, headers=API_KEY_HEADER)
    r.raise_for_status()
    return r.json()

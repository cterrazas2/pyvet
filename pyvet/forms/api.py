"""
Forms API: https://developer.va.gov/explore/vaForms/docs/vaForms?version=current
"""
import logging
import requests

from pyvet.creds import API_URL
from pyvet.client import current_session as session

FORMS_URL = API_URL + "va_forms/v0/forms"


def get_forms(query: str = ""):
    """Gets forms or filtered with optional params.
    Parameters
    ----------
    query : str
        The query to find forms.

    Returns
    -------
    """
    params = dict(query=query)
    try:
        r = session.get(FORMS_URL, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)


def get_form(form_name="10-10EZ"):
    """Gets a form based on a form name
    Parameters
    ----------
    form_name : str
        The target form name to retrieve.
    Returns
    -------
    r : json
        Response in json format.
    """
    params = dict(form_name=form_name)
    form_url = FORMS_URL + "/" + form_name
    try:
        r = session.get(form_url, params=params)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.RequestException as e:
        logging.error(e)

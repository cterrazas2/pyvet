"""
Forms API: https://developer.va.gov/explore/vaForms/docs/vaForms?version=current
"""
import logging
import requests

from pyvet.creds import API_KEY_HEADER, API_URL

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
    retries = 0
    params = dict(query=query)
    try:
        r = requests.get(FORMS_URL, params=params, headers=API_KEY_HEADER)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.info(f"Connection timeout, retry #{retries}")
            get_forms(query)
        else:
            print(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
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
    retries = 0
    params = dict(form_name=form_name)
    form_url = FORMS_URL + "/" + form_name
    try:
        r = requests.get(form_url, params=params, headers=API_KEY_HEADER)
        r.raise_for_status()
        r = r.json()
        return r
    except requests.exceptions.Timeout as e:
        if retries < 4:
            retries += 1
            logging.info(f"Connection timeout, retry #{retries}")
            get_form(form_name)
        else:
            print(e)
    except requests.exceptions.TooManyRedirects as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)

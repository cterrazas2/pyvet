import unittest
from requests import Session
from pyvet import creds
from pyvet.forms.api import get_form, get_forms

from tests.data.mock_forms_data import MOCK_FORM, MOCK_FORMS
from unittest.mock import patch


@patch.object(Session, "get", headers=creds.API_KEY_HEADER)
class TestForms(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER
        self.forms_url = creds.VA_SANDBOX_API + "va_forms/v0/forms"

    def test_get_form(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_FORM
        assert mock_get.headers == self.headers
        mock_form_name = "vha_506"
        form = get_form(form_name=mock_form_name)
        self.assertDictEqual(form, MOCK_FORM)
        mock_get.assert_called_once_with(
            self.forms_url + f"/{mock_form_name}",
            params={"form_name": mock_form_name},
        )

    def test_get_forms(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_FORMS
        assert mock_get.headers == self.headers
        all_forms = get_forms()
        self.assertDictEqual(all_forms, MOCK_FORMS)
        mock_get.assert_called_once_with(
            self.forms_url,
            params={"query": None},
        )


if __name__ == "__main__":
    unittest.main()

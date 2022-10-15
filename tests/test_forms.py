import json
import unittest
from pyvet import creds
from pyvet import forms

from tests.data.mock_forms_data import MOCK_FORM, MOCK_FORMS
from unittest.mock import patch

form_json = json.loads(MOCK_FORM)
forms_json = json.loads(MOCK_FORMS)


class TestForms(unittest.TestCase):
    def setUp(self):
        self.api_key = creds.API_KEY
        self.forms_url = creds.VA_SANDBOX_API + "va_forms/v0/forms"

    @patch("pyvet.forms.requests.get")
    def test_get_form(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = form_json
        mock_form_name = "vha_506"
        form = forms.get_form(form_name=mock_form_name)
        self.assertDictEqual(form, form_json)
        mock_get.assert_called_once_with(
            self.forms_url + f"/{mock_form_name}",
            params=dict(form_name=mock_form_name),
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.forms.requests.get")
    def test_get_forms(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = forms_json

        all_forms = forms.get_forms()
        self.assertDictEqual(all_forms, forms_json)
        mock_get.assert_called_once_with(
            self.forms_url,
            params=dict(query=""),
            headers=dict(apiKey=self.api_key),
        )


if __name__ == "__main__":
    unittest.main()

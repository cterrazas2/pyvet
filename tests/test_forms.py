import unittest
from pyvet import creds
from pyvet.forms.api import get_form, get_forms

from tests.data.mock_forms_data import MOCK_FORM, MOCK_FORMS
from unittest.mock import patch


class TestForms(unittest.TestCase):
    def setUp(self):
        self.api_key = creds.API_KEY
        self.forms_url = creds.VA_SANDBOX_API + "va_forms/v0/forms"

    @patch("pyvet.forms.api.requests.get")
    def test_get_form(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_FORM
        mock_form_name = "vha_506"
        form = get_form(form_name=mock_form_name)
        self.assertDictEqual(form, MOCK_FORM)
        mock_get.assert_called_once_with(
            self.forms_url + f"/{mock_form_name}",
            params=dict(form_name=mock_form_name),
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.forms.api.requests.get")
    def test_get_forms(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_FORMS

        all_forms = get_forms()
        self.assertDictEqual(all_forms, MOCK_FORMS)
        mock_get.assert_called_once_with(
            self.forms_url,
            params=dict(query=""),
            headers=dict(apiKey=self.api_key),
        )


if __name__ == "__main__":
    unittest.main()

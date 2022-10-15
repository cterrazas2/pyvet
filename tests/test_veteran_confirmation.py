import unittest
from pyvet import creds
from pyvet.veteran_confirmation.api import get_status

from unittest.mock import patch

mock_confirmed = dict(veteran_status="confirmed")


class TestVeteranConfirmation(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER
        self.confirmation_url = creds.VA_SANDBOX_API + "veteran_confirmation/v0/"

    @patch("pyvet.veteran_confirmation.api.requests.post")
    def test_get_status(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_confirmed
        vet_status = get_status(
            ssn="796-13-0115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
            middle_name="E",
            gender="F",
        )
        self.assertDictEqual(vet_status, mock_confirmed)
        mock_get.assert_called_once_with(
            self.confirmation_url + "status",
            json=dict(
                ssn="796-13-0115",
                first_name="Tamara",
                last_name="Ellis",
                birth_date="1967-06-19",
                middle_name="E",
                gender="F",
            ),
            headers=self.headers,
        )


if __name__ == "__main__":
    unittest.main()

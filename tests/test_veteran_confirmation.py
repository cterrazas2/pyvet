import unittest
from pyvet import creds
from pyvet.veteran_confirmation.api import get_status
from requests import Session

from unittest.mock import patch

mock_confirmed = dict(veteran_status="confirmed")


@patch.object(Session, "post", headers=creds.API_KEY_HEADER)
class TestVeteranConfirmation(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER
        self.confirmation_url = creds.VA_SANDBOX_API + "veteran_confirmation/v0/"

    def test_get_status(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_confirmed
        assert mock_post.headers == self.headers
        vet_status = get_status(
            ssn="796-13-0115",
            first_name="Tamara",
            last_name="Ellis",
            birth_date="1967-06-19",
            middle_name="E",
            gender="F",
        )
        self.assertDictEqual(vet_status, mock_confirmed)
        mock_post.assert_called_once_with(
            self.confirmation_url + "status",
            json=dict(
                ssn="796-13-0115",
                first_name="Tamara",
                last_name="Ellis",
                birth_date="1967-06-19",
                middle_name="E",
                gender="F",
            ),
        )


if __name__ == "__main__":
    unittest.main()

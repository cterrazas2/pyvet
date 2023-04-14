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
        self.confirmation_url = creds.VA_SANDBOX_API + "veteran-confirmation/v1/"

    def test_get_status(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_confirmed
        assert mock_post.headers == self.headers
        vet_status = get_status(
            first_name="Alfredo",
            last_name="Armstrong",
            birth_date="1993-06-08",
            middle_name="M",
            gender="M",
            street_address="17020 Tortoise St",
            city="Round Rock",
            zip_code="78664",
            state="TX",
            country="USA",
            home_phone_number="555-555-5555",
            mothers_maiden_mame="Smith",
            birth_place_city="Johnson City",
            birth_place_state="MA",
            birth_place_country="USA",
        )
        self.assertDictEqual(vet_status, mock_confirmed)
        mock_post.assert_called_once_with(
            self.confirmation_url + "status",
            json=dict(
                firstName="Alfredo",
                lastName="Armstrong",
                birthDate="1993-06-08",
                middleName="M",
                gender="M",
                streetAddressLine1="17020 Tortoise St",
                city="Round Rock",
                zipCode="78664",
                state="TX",
                country="USA",
                homePhoneNumber="555-555-5555",
                mothersMaidenName="Smith",
                birthPlaceCity="Johnson City",
                birthPlaceState="MA",
                birthPlaceCountry="USA",
            ),
        )


if __name__ == "__main__":
    unittest.main()

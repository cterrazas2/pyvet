"""
TO-DO: get_facilities_bbox(
"""

import json
import unittest
from pyvet import creds
from pyvet import facilities
from tests.data.mock_facilities import (
    MOCK_FACILITY,
    MOCK_FACILITIES,
    MOCK_FACILITY_IDS,
    MOCK_NEARBY,
)
from unittest.mock import patch

facilities_json = json.loads(MOCK_FACILITIES)
facility_ids_json = json.loads(MOCK_FACILITY_IDS)
facility_json = json.loads(MOCK_FACILITY)
nearby_json = json.loads(MOCK_NEARBY)


class TestFacility(unittest.TestCase):
    def setUp(self):
        self.api_key = creds.API_KEY
        self.facilities_url = creds.VA_SANDBOX_API + "va_facilities/v0/"

    @patch("pyvet.facilities.requests.get")
    def test_get_facility(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = facility_json
        mock_id = "vha_506"
        facility = facilities.get_facility(f_id=mock_id)
        self.assertDictEqual(facility, facility_json)
        mock_get.assert_called_once_with(
            self.facilities_url + f"facilities/{mock_id}",
            params=dict(id=mock_id),
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.facilities.requests.get")
    def test_get_facilities(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = facilities_json

        all_facilities = facilities.get_all(print_csv_file=False)
        self.assertDictEqual(all_facilities, facilities_json)
        mock_get.assert_called_once_with(
            self.facilities_url + "facilities/all",
            params=dict(Accept="application/geo+json"),
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.facilities.requests.get")
    def test_get_facility_ids(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = facility_ids_json

        all_facility_ids = facilities.get_ids()
        self.assertDictEqual(all_facility_ids, facility_ids_json)
        mock_get.assert_called_once_with(
            self.facilities_url + "ids",
            params=dict(type="health"),
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.facilities.requests.get")
    def test_nearby_facilities(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = nearby_json
        mock_address = ""
        mock_city = "Boston"
        mock_state = "MA"
        mock_zip = "02108"
        mock_drive_time = 60
        nearby_facilities = facilities.get_nearby(
            address=mock_address,
            city=mock_city,
            state=mock_state,
            zip_code=mock_zip,
            drive_time=mock_drive_time,
        )
        self.assertDictEqual(nearby_facilities, nearby_json)
        mock_get.assert_called_once_with(
            self.facilities_url + "nearby",
            params=dict(
                street_address=mock_address,
                city=mock_city,
                state=mock_state,
                zip=mock_zip,
                drive_time=mock_drive_time,
            ),
            headers=dict(apiKey=self.api_key),
        )


if __name__ == "__main__":
    unittest.main()

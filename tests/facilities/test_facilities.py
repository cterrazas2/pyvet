import unittest
from requests import Session
from pyvet import creds
from pyvet.facilities.api import (
    get_all,
    get_facilities_by_query,
    get_facility,
    get_ids,
    get_nearby,
)
from tests.data.mock_facilities import (
    MOCK_FACILITY,
    MOCK_FACILITIES,
    MOCK_FACILITY_IDS,
    MOCK_NEARBY,
    MOCK_QUERY_JSON,
)
from unittest.mock import patch


@patch.object(Session, "get", headers=creds.API_KEY_HEADER)
class TestFacilities(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER
        self.facilities_url = creds.VA_SANDBOX_API + "va_facilities/v0/"

    def test_get_facility(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_FACILITY
        assert mock_get.headers == self.headers
        mock_id = "vha_506"
        facility = get_facility(f_id=mock_id)
        self.assertDictEqual(facility, MOCK_FACILITY)
        mock_get.assert_called_once_with(
            self.facilities_url + f"facilities/{mock_id}",
            params=dict(id=mock_id),
        )

    def test_get_facilities(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_FACILITIES

        all_facilities = get_all(export_csv_file=False)
        self.assertDictEqual(all_facilities, MOCK_FACILITIES)
        mock_get.assert_called_once_with(
            self.facilities_url + "facilities/all",
            params=dict(Accept="application/geo+json"),
        )

    def test_get_facility_ids(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_FACILITY_IDS

        all_facility_ids = get_ids()
        self.assertDictEqual(all_facility_ids, MOCK_FACILITY_IDS)
        mock_get.assert_called_once_with(
            self.facilities_url + "ids",
            params=dict(type="health"),
        )

    def test_nearby_facilities(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_NEARBY
        mock_address = ""
        mock_city = "Boston"
        mock_state = "MA"
        mock_zip = "02108"
        mock_drive_time = 60
        nearby_facilities = get_nearby(
            address=mock_address,
            city=mock_city,
            state=mock_state,
            zip_code=mock_zip,
            drive_time=mock_drive_time,
        )
        self.assertDictEqual(nearby_facilities, MOCK_NEARBY)
        mock_get.assert_called_once_with(
            self.facilities_url + "nearby",
            params=dict(
                street_address=mock_address,
                city=mock_city,
                state=mock_state,
                zip=mock_zip,
                drive_time=mock_drive_time,
            ),
        )

    def test_facilities_invalid_query(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_QUERY_JSON
        queried_facilities = get_facilities_by_query(
            bbox=[-105.4, 39.4, -104.5, 40.1],
            latitude=56.7,
            longitude=-123.4,
            ids=["vha_688", "vha_644"],
            facility_type="health",
            services=[],
            mobile=False,
        )
        self.assertIsNone(queried_facilities)
        mock_get.assert_not_called()

    def test_facilities_ids_query(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_QUERY_JSON
        queried_facilities = get_facilities_by_query(
            ids=["vha_688", "vha_644"],
            facility_type="health",
            services=[],
            mobile=False,
        )
        self.assertDictEqual(queried_facilities, MOCK_QUERY_JSON)
        mock_get.assert_called_once_with(
            self.facilities_url + "facilities",
            params=dict(
                bbox=None,
                ids=["vha_688", "vha_644"],
                lat=None,
                long=None,
                radius=None,
                type="health",
                services=[],
                mobile=False,
                state=None,
                visn=None,
                zip=None,
                page=1,
                per_page=30,
            ),
        )

    def test_facilities_lat_lon_query(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_QUERY_JSON
        queried_facilities = get_facilities_by_query(
            ids=["vha_688", "vha_644"],
            latitude=56.7,
            longitude=-123.4,
            radius=10.0,
            facility_type="health",
            services=[],
            mobile=False,
        )
        self.assertDictEqual(queried_facilities, MOCK_QUERY_JSON)
        mock_get.assert_called_once_with(
            self.facilities_url + "facilities",
            params=dict(
                bbox=None,
                ids=["vha_688", "vha_644"],
                lat=56.7,
                long=-123.4,
                radius=10.0,
                type="health",
                services=[],
                mobile=False,
                state=None,
                visn=None,
                zip=None,
                page=1,
                per_page=30,
            ),
        )

    def test_facilities_bbox_query(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_QUERY_JSON
        queried_facilities = get_facilities_by_query(
            bbox=[-105.4, 39.4, -104.5, 40.1],
            ids=["vha_688", "vha_644"],
            facility_type="health",
            services=[],
            mobile=True,
        )
        self.assertDictEqual(queried_facilities, MOCK_QUERY_JSON)
        mock_get.assert_called_once_with(
            self.facilities_url + "facilities",
            params=dict(
                bbox=[-105.4, 39.4, -104.5, 40.1],
                ids=["vha_688", "vha_644"],
                lat=None,
                long=None,
                radius=None,
                type="health",
                services=[],
                mobile=True,
                state=None,
                visn=None,
                zip=None,
                page=1,
                per_page=30,
            ),
        )

    def test_facilities_state_query(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_QUERY_JSON
        queried_facilities = get_facilities_by_query(
            ids=["vha_688", "vha_644"],
            facility_type="health",
            services=[],
            mobile=True,
            state="CA",
        )
        self.assertDictEqual(queried_facilities, MOCK_QUERY_JSON)
        mock_get.assert_called_once_with(
            self.facilities_url + "facilities",
            params=dict(
                bbox=None,
                ids=["vha_688", "vha_644"],
                lat=None,
                long=None,
                radius=None,
                type="health",
                services=[],
                mobile=True,
                state="CA",
                visn=None,
                zip=None,
                page=1,
                per_page=30,
            ),
        )

    def test_facilities_zip_code_query(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_QUERY_JSON
        queried_facilities = get_facilities_by_query(
            ids=["vha_688", "vha_644"],
            facility_type="health",
            services=[],
            mobile=True,
            zip_code="80301",
        )
        self.assertDictEqual(queried_facilities, MOCK_QUERY_JSON)
        mock_get.assert_called_once_with(
            self.facilities_url + "facilities",
            params=dict(
                bbox=None,
                ids=["vha_688", "vha_644"],
                lat=None,
                long=None,
                radius=None,
                type="health",
                services=[],
                mobile=True,
                state=None,
                visn=None,
                zip="80301",
                page=1,
                per_page=30,
            ),
        )

    def test_facilities_visn_query(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_QUERY_JSON
        queried_facilities = get_facilities_by_query(
            ids=["vha_688", "vha_644"],
            services=[],
            mobile=True,
            visn=26,
        )
        self.assertDictEqual(queried_facilities, MOCK_QUERY_JSON)
        mock_get.assert_called_once_with(
            self.facilities_url + "facilities",
            params=dict(
                bbox=None,
                ids=["vha_688", "vha_644"],
                lat=None,
                long=None,
                radius=None,
                type=None,
                services=[],
                mobile=True,
                state=None,
                visn=26,
                zip=None,
                page=1,
                per_page=30,
            ),
        )


if __name__ == "__main__":
    unittest.main()

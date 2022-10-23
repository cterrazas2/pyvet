import unittest
from pyvet import creds
from pyvet.health.api import (
    get_location,
    get_location_by_id,
    get_organization,
    get_organization_by_id,
    get_practitioner,
    get_practitioner_by_id,
    get_practitioner_role,
    get_practitioner_role_by_id,
)
from tests.data.mock_health_data import (
    MOCK_ORG,
    MOCK_ORG_ID,
    MOCK_LOCATION,
    MOCK_LOCATION_ID,
    MOCK_PRACTITIONER,
    MOCK_PRACTITIONER_ID,
    MOCK_PRACTITIONER_ROLE,
    MOCK_PRACTITIONER_ROLE_ID,
)
from unittest.mock import patch


class TestHealthProviderDirectory(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER
        self.health_url = creds.VA_SANDBOX_API + "provider-directory/v0/r4/"

    @patch("pyvet.health.api.requests.get")
    def test_get_location(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_LOCATION
        mock_params = dict(
            practitioner_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            identifier="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            address="151 KNOLLCROFT ROAD",
            city="LYONS",
            state="NJ",
            zip_code="07939",
            name="VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB",
            page=1,
            count=30,
        )
        location = get_location(**mock_params)
        self.assertDictEqual(location, MOCK_LOCATION)
        mock_get.assert_called_once_with(
            self.health_url + "Location",
            params={
                "_id": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "identifier": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "address": "151 KNOLLCROFT ROAD",
                "address-city": "LYONS",
                "address-state": "NJ",
                "address-postalcode": "07939",
                "name": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB",
                "page": 1,
                "_count": 30,
            },
            headers=self.headers,
        )

    @patch("pyvet.health.api.requests.get")
    def test_get_location_by_id(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_LOCATION_ID
        mock_id = "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000"
        location = get_location_by_id(resource_id=mock_id)
        self.assertDictEqual(location, MOCK_LOCATION_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Location/{mock_id}",
            headers=self.headers,
        )

    @patch("pyvet.health.api.requests.get")
    def test_get_organization(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_ORG
        mock_params = dict(
            org_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            identifier="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            address="2360 E PERSHING BLVD",
            city="CHEYENNE",
            state="WY",
            zip_code="82001",
            name="CHEYENNE VA MEDICAL",
            page=1,
            count=30,
        )
        organization = get_organization(**mock_params)
        self.assertDictEqual(organization, MOCK_ORG)
        mock_get.assert_called_once_with(
            self.health_url + "Organization",
            params={
                "_id": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "identifier": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "address": "2360 E PERSHING BLVD",
                "address-city": "CHEYENNE",
                "address-state": "WY",
                "address-postalcode": "82001",
                "name": "CHEYENNE VA MEDICAL",
                "page": 1,
                "_count": 30,
            },
            headers=self.headers,
        )

    @patch("pyvet.health.api.requests.get")
    def test_get_organization_by_id(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_ORG_ID
        mock_id = "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000"
        organization = get_organization_by_id(org_id=mock_id)
        self.assertDictEqual(organization, MOCK_ORG_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Organization/{mock_id}",
            headers=self.headers,
        )

    @patch("pyvet.health.api.requests.get")
    def test_get_practitioner(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PRACTITIONER
        mock_params = dict(
            resource_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            prac_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            family="DOE922",
            given="JANE460",
            name="DOE922",
            page=1,
            count=30,
        )
        practitioner = get_practitioner(**mock_params)
        self.assertDictEqual(practitioner, MOCK_PRACTITIONER)
        mock_get.assert_called_once_with(
            self.health_url + "Practitioner",
            params={
                "_id": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "identifier": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "family": "DOE922",
                "given": "JANE460",
                "name": "DOE922",
                "page": 1,
                "_count": 30,
            },
            headers=self.headers,
        )

    @patch("pyvet.health.api.requests.get")
    def test_get_practitioner_by_id(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PRACTITIONER_ID
        mock_id = "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000"
        practitioner = get_practitioner_by_id(pr_id=mock_id)
        self.assertDictEqual(practitioner, MOCK_PRACTITIONER_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Practitioner/{mock_id}",
            headers=self.headers,
        )

    @patch("pyvet.health.api.requests.get")
    def test_get_practitioner_role(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PRACTITIONER_ROLE
        mock_params = dict(
            resource_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            prac_id="I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            prac_name="DOE922",
            page=1,
            count=30,
        )
        practitioner = get_practitioner_role(**mock_params)
        self.assertDictEqual(practitioner, MOCK_PRACTITIONER_ROLE)
        mock_get.assert_called_once_with(
            self.health_url + "PractitionerRole",
            params={
                "_id": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "practitioner.identifier": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "practitioner.name": "DOE922",
                "page": 1,
                "_count": 30,
            },
            headers=self.headers,
        )

    @patch("pyvet.health.api.requests.get")
    def test_get_practitioner_role_by_id(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PRACTITIONER_ROLE_ID
        mock_id = "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000"
        practitioner = get_practitioner_role_by_id(pr_role_id=mock_id)
        self.assertDictEqual(practitioner, MOCK_PRACTITIONER_ROLE_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"PractitionerRole/{mock_id}",
            headers=self.headers,
        )


if __name__ == "__main__":
    unittest.main()

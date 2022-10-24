import unittest
from requests import Session
from pyvet import creds
from pyvet.benefits_reference.api import (
    get_disabilities,
    get_contention_types,
    get_countries,
    get_intake_sites,
    get_military_pay_types,
    get_service_branches,
    get_special_circumstances,
    get_states,
    get_treatment_centers,
)
from tests.data.mock_benefits_reference import (
    MOCK_CONTENTION,
    MOCK_COUNTRIES,
    MOCK_DISABILITIES_DATA,
    MOCK_INTAKE_SITES,
    MOCK_MILITARY_PAY_TYPES,
    MOCK_SERVICE_BRANCES,
    MOCK_SPECIAL_CIRCUMSTANCES,
    MOCK_STATES,
    MOCK_TREATMENT_CENTERS,
)
from unittest.mock import patch


@patch.object(Session, "get", headers=creds.API_KEY_HEADER)
class TestBenefitsReference(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER
        self.benefits_reference_url = (
            creds.VA_SANDBOX_API + "benefits-reference-data/v1/"
        )

    def test_get_contention_types(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_CONTENTION
        assert mock_get.headers == self.headers
        contention_types = get_contention_types()
        self.assertDictEqual(contention_types, MOCK_CONTENTION)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "contention-types",
        )

    def test_get_countries(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_COUNTRIES
        assert mock_get.headers == self.headers
        countries = get_countries()
        self.assertDictEqual(countries, MOCK_COUNTRIES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "countries",
        )

    def test_get_disabilities(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DISABILITIES_DATA
        assert mock_get.headers == self.headers
        disabilities = get_disabilities()
        self.assertDictEqual(disabilities, MOCK_DISABILITIES_DATA)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "disabilities",
        )

    def test_get_intake_sites(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_INTAKE_SITES
        assert mock_get.headers == self.headers
        intake_sites = get_intake_sites()
        self.assertDictEqual(intake_sites, MOCK_INTAKE_SITES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "intake-sites",
        )

    def test_get_military_pay_types(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_MILITARY_PAY_TYPES
        assert mock_get.headers == self.headers
        mil_pay_types = get_military_pay_types()
        self.assertDictEqual(mil_pay_types, MOCK_MILITARY_PAY_TYPES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "military-pay-types",
        )

    def test_get_service_branches(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_SERVICE_BRANCES
        assert mock_get.headers == self.headers
        branches = get_service_branches()
        self.assertDictEqual(branches, MOCK_SERVICE_BRANCES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "service-branches",
        )

    def test_get_special_circumstances(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_SPECIAL_CIRCUMSTANCES
        assert mock_get.headers == self.headers
        special = get_special_circumstances()
        self.assertDictEqual(special, MOCK_SPECIAL_CIRCUMSTANCES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "special-circumstances",
        )

    def test_get_states(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_STATES
        assert mock_get.headers == self.headers
        states = get_states()
        self.assertDictEqual(states, MOCK_STATES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "states",
        )

    def test_get_treatment_centers(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_TREATMENT_CENTERS
        assert mock_get.headers == self.headers
        centers = get_treatment_centers()
        self.assertDictEqual(centers, MOCK_TREATMENT_CENTERS)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "treatment-centers",
        )


if __name__ == "__main__":
    unittest.main()

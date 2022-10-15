import unittest
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


class BenefitsReference(unittest.TestCase):
    def setUp(self):
        self.api_key = creds.API_KEY
        self.benefits_reference_url = (
            creds.VA_SANDBOX_API + "benefits-reference-data/v1/"
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_contention_types(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_CONTENTION
        contention_types = get_contention_types()
        self.assertDictEqual(contention_types, MOCK_CONTENTION)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "contention-types",
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_countries(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_COUNTRIES

        countries = get_countries()
        self.assertDictEqual(countries, MOCK_COUNTRIES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "countries",
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_disabilities(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DISABILITIES_DATA

        disabilities = get_disabilities()
        self.assertDictEqual(disabilities, MOCK_DISABILITIES_DATA)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "disabilities",
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_intake_sites(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_INTAKE_SITES

        intake_sites = get_intake_sites()
        self.assertDictEqual(intake_sites, MOCK_INTAKE_SITES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "intake-sites",
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_military_pay_types(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_MILITARY_PAY_TYPES

        mil_pay_types = get_military_pay_types()
        self.assertDictEqual(mil_pay_types, MOCK_MILITARY_PAY_TYPES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "military-pay-types",
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_service_branches(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_SERVICE_BRANCES

        branches = get_service_branches()
        self.assertDictEqual(branches, MOCK_SERVICE_BRANCES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "service-branches",
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_special_circumstances(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_SPECIAL_CIRCUMSTANCES

        special = get_special_circumstances()
        self.assertDictEqual(special, MOCK_SPECIAL_CIRCUMSTANCES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "special-circumstances",
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_states(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_STATES

        states = get_states()
        self.assertDictEqual(states, MOCK_STATES)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "states",
            headers=dict(apiKey=self.api_key),
        )

    @patch("pyvet.benefits_reference.api.requests.get")
    def test_get_treatment_centers(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_TREATMENT_CENTERS

        centers = get_treatment_centers()
        self.assertDictEqual(centers, MOCK_TREATMENT_CENTERS)
        mock_get.assert_called_once_with(
            self.benefits_reference_url + "treatment-centers",
            headers=dict(apiKey=self.api_key),
        )


if __name__ == "__main__":
    unittest.main()

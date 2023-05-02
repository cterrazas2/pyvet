import unittest
from requests import Session
from pyvet import creds

from pyvet.health.patient_health.api import (
    get_allergy_intolerance,
    get_allergy_intolerance_by_id,
    get_appointment,
    get_appointment_by_id,
    get_binary_by_id,
    get_condition,
    get_condition_by_id,
    get_device,
    get_device_by_id,
    get_device_request,
    get_device_request_by_id,
    get_diagnostic_report,
    get_diagnostic_report_by_id,
    get_document_reference,
    get_document_reference_by_id,
    get_encounter,
    get_encounter_by_id,
    get_immunization,
    get_immunization_by_id,
    get_location,
    get_location_by_id,
    get_medication,
    get_medication_by_id,
    get_medication_request,
    get_medication_request_by_id,
    get_observation,
    get_observation_by_id,
    get_organization,
    get_organization_by_id,
    get_patient,
    get_patient_by_id,
    get_practitioner,
    get_practitioner_by_id,
    get_practitioner_role,
    get_practitioner_role_by_id,
    get_procedure,
    get_procedure_by_id,
    get_metadata,
)

from tests.data.mock_patient_data import (
    MOCK_ALLERGY_INTOLERANCE,
    MOCK_ALLERGY_INTOLERANCE_ID,
    MOCK_APPOINTMENT,
    MOCK_APPOINTMENT_ID,
    MOCK_BINARY_ID,
    MOCK_CONDITION,
    MOCK_CONDITION_ID,
    MOCK_DEVICE,
    MOCK_DEVICE_ID,
    MOCK_DEVICE_REQUEST,
    MOCK_DEVICE_REQUEST_ID,
    MOCK_DIAGNOSTIC_REPORT,
    MOCK_DIAGNOSTIC_REPORT_ID,
    MOCK_DOCUMENT_REFERENCE,
    MOCK_DOCUMENT_REFERENCE_ID,
    MOCK_ENCOUNTER,
    MOCK_ENCOUNTER_ID,
    MOCK_IMMUNIZATION,
    MOCK_IMMUNIZATION_ID,
    MOCK_LOCATION,
    MOCK_LOCATION_ID,
    MOCK_MEDICATION,
    MOCK_MEDICATION_ID,
    MOCK_MEDICATION_REQUEST,
    MOCK_MEDICATION_REQUEST_ID,
    MOCK_OBSERVATION,
    MOCK_OBSERVATION_ID,
    MOCK_ORGANIZATION,
    MOCK_ORGANIZATION_ID,
    MOCK_PATIENT,
    MOCK_PATIENT_ID,
    MOCK_PRACTITIONER,
    MOCK_PRACTITIONER_ID,
    MOCK_PRACTITIONER_ROLE,
    MOCK_PRACTITIONER_ROLE_ID,
    MOCK_PROCEDURE,
    MOCK_PROCEDURE_ID,
    MOCK_METADATA,
)

from unittest.mock import patch


@patch(
    "pyvet.health.patient_health.api.get_bearer_token",
    return_value="somerandomtoken",
)
@patch.object(Session().headers, "get", return_value=None)
@patch.object(Session, "get", headers={"apiKey": creds.API_KEY_HEADER.get("apiKey")})
class TestHealthPatient(unittest.TestCase):
    def setUp(self):
        self.headers = {"apiKey": creds.API_KEY_HEADER.get("apiKey")}
        self.health_url = creds.VA_SANDBOX_API + "fhir/v0/r4/"
        # we use one session so we reset the token here if it's been set by another test globally.
        creds.API_KEY_HEADER["Authorization"] = None

    def test_get_allergy_intolerance(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_ALLERGY_INTOLERANCE
        assert mock_auth.return_value == None
        allergy_intolerance = get_allergy_intolerance()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(allergy_intolerance, MOCK_ALLERGY_INTOLERANCE)
        mock_get.assert_called_once_with(
            self.health_url + "AllergyIntolerance",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_allergy_intolerance_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_ALLERGY_INTOLERANCE_ID
        assert mock_auth.return_value == None
        mock_id = "I2-FY4N5GUAQ4IZQVQZUPDFN43S4A000000"
        allergy_intolerance = get_allergy_intolerance_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(allergy_intolerance, MOCK_ALLERGY_INTOLERANCE_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"AllergyIntolerance/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_appointment(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_APPOINTMENT
        assert mock_auth.return_value == None
        appointment = get_appointment()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(appointment, MOCK_APPOINTMENT)
        mock_get.assert_called_once_with(
            self.health_url + "Appointment",
            headers={
                "apiKey": creds.API_KEY_HEADER.get("apiKey"),
                "Authorization": "Bearer somerandomtoken",
            },
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "location": None,
                "_lastUpdated": None,
                "date": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_appointment_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_APPOINTMENT_ID
        assert mock_auth.return_value == None
        mock_id = "I2-V7QE6HNG7MXDOIEWC534Y3HRYWKJGRCGJSVDZW7YDHXR7RMD2FWA0000"
        appointment = get_appointment_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(appointment, MOCK_APPOINTMENT_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Appointment/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_binary_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_BINARY_ID
        assert mock_auth.return_value == None
        mock_id = "4-10cM2Q9dqjfi52cS61pfSBhDWrpLiQiSAJ4MGNtHN"
        binary_id = get_binary_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(binary_id, MOCK_BINARY_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Binary/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_condition(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_CONDITION
        assert mock_auth.return_value == None
        condition = get_condition()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(condition, MOCK_CONDITION)
        mock_get.assert_called_once_with(
            self.health_url + "Condition",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "category": None,
                "clinical-status": None,
                "code": None,
                "onset-date": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_condition_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_CONDITION_ID
        assert mock_auth.return_value == None
        mock_id = "I2-TWYEPQNF7H5A4OG5P3SW55FP44000000"
        condition = get_condition_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(condition, MOCK_CONDITION_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Condition/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_device(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DEVICE
        assert mock_auth.return_value == None
        device = get_device()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(device, MOCK_DEVICE)
        mock_get.assert_called_once_with(
            self.health_url + "Device",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "type": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_device_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DEVICE_ID
        assert mock_auth.return_value == None
        mock_id = "I2-DPWVDPSF36SDG527A43QRGHKUU5G2VYK5KITXOWUDY222Q5ZOJJQ0000"
        device = get_device_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(device, MOCK_DEVICE_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Device/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_device_request(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DEVICE_REQUEST
        assert mock_auth.return_value == None
        device_request = get_device_request()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(device_request, MOCK_DEVICE_REQUEST)
        mock_get.assert_called_once_with(
            self.health_url + "DeviceRequest",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_device_request_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DEVICE_REQUEST_ID
        assert mock_auth.return_value == None
        mock_id = "I2-UFT532RWEIOS2WWZQWXUB7TKCT5SODPVTQJQD3ZNZUSAXXB4KZXQ0000"
        device_request = get_device_request_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(device_request, MOCK_DEVICE_REQUEST_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"DeviceRequest/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_diagnostic_report(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DIAGNOSTIC_REPORT
        assert mock_auth.return_value == None
        diagnostic_report = get_diagnostic_report()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(diagnostic_report, MOCK_DIAGNOSTIC_REPORT)
        mock_get.assert_called_once_with(
            self.health_url + "DiagnosticReport",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "category": None,
                "code": None,
                "date": None,
                "status": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_diagnostic_report_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DIAGNOSTIC_REPORT_ID
        assert mock_auth.return_value == None
        mock_id = "I2-UFT532RWEIOS2WWZQWXUB7TKCT5SODPVTQJQD3ZNZUSAXXB4KZXQ0000"
        diagnostic_report = get_diagnostic_report_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(diagnostic_report, MOCK_DIAGNOSTIC_REPORT_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"DiagnosticReport/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_document_reference(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DOCUMENT_REFERENCE
        assert mock_auth.return_value == None
        document_reference = get_document_reference()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(document_reference, MOCK_DOCUMENT_REFERENCE)
        mock_get.assert_called_once_with(
            self.health_url + "DocumentReference",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "type": None,
                "date": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_document_reference_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_DOCUMENT_REFERENCE_ID
        assert mock_auth.return_value == None
        mock_id = "I2-UFT532RWEIOS2WWZQWXUB7TKCT5SODPVTQJQD3ZNZUSAXXB4KZXQ0000"
        document_reference = get_document_reference_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(document_reference, MOCK_DOCUMENT_REFERENCE_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"DocumentReference/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_encounter(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_ENCOUNTER
        assert mock_auth.return_value == None
        encounter = get_encounter()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(encounter, MOCK_ENCOUNTER)
        mock_get.assert_called_once_with(
            self.health_url + "Encounter",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "date": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_encounter_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_ENCOUNTER_ID
        assert mock_auth.return_value == None
        mock_id = "I2-5WR43OIGY4625GCVOZTBYODWIEVVWLDDWEDSXUTTHZCTHKKBIDTQ0000"
        encounter = get_encounter_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(encounter, MOCK_ENCOUNTER_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Encounter/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_immunization(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_IMMUNIZATION
        assert mock_auth.return_value == None
        immunization = get_immunization()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(immunization, MOCK_IMMUNIZATION)
        mock_get.assert_called_once_with(
            self.health_url + "Immunization",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_immunization_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_IMMUNIZATION_ID
        assert mock_auth.return_value == None
        mock_id = "I2-5ED3EJGWQMUZVD56BEK252R5UM000000"
        immunization = get_immunization_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(immunization, MOCK_IMMUNIZATION_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Immunization/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_location(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_LOCATION
        assert mock_auth.return_value == None
        location = get_location()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(location, MOCK_LOCATION)
        mock_get.assert_called_once_with(
            self.health_url + "Location",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "address-city": None,
                "address-state": None,
                "address-postal-code": None,
                "name": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_location_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_LOCATION_ID
        assert mock_auth.return_value == None
        mock_id = "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000"
        location = get_location_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(location, MOCK_LOCATION_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Location/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_medication(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_MEDICATION
        assert mock_auth.return_value == None
        medication = get_medication()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(medication, MOCK_MEDICATION)
        mock_get.assert_called_once_with(
            self.health_url + "Medication",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_medication_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_MEDICATION_ID
        assert mock_auth.return_value == None
        mock_id = "I2-EKB436MCBFA2QLFPGWSBO66SP4000000"
        medication = get_medication_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(medication, MOCK_MEDICATION_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Medication/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_medication_request(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_MEDICATION_REQUEST
        assert mock_auth.return_value == None
        medication_request = get_medication_request()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(medication_request, MOCK_MEDICATION_REQUEST)
        mock_get.assert_called_once_with(
            self.health_url + "MedicationRequest",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "_lastUpdated": None,
                "intent": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_medication_request_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_MEDICATION_REQUEST_ID
        assert mock_auth.return_value == None
        mock_id = "I2-EKB436MCBFA2QLFPGWSBO66SP4000000"
        medication_request = get_medication_request_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(medication_request, MOCK_MEDICATION_REQUEST_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"MedicationRequest/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_observation(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_OBSERVATION
        assert mock_auth.return_value == None
        observation = get_observation()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(observation, MOCK_OBSERVATION)
        mock_get.assert_called_once_with(
            self.health_url + "Observation",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "category": None,
                "code": None,
                "date": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_observation_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_OBSERVATION_ID
        assert mock_auth.return_value == None
        mock_id = "I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000"
        observation = get_observation_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(observation, MOCK_OBSERVATION_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Observation/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_organization(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_ORGANIZATION
        assert mock_auth.return_value == None
        organization = get_organization()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(organization, MOCK_ORGANIZATION)
        mock_get.assert_called_once_with(
            self.health_url + "Organization",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "address-city": None,
                "address-state": None,
                "address-postal-code": None,
                "name": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_organization_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_ORGANIZATION_ID
        assert mock_auth.return_value == None
        mock_id = "I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000"
        organization = get_organization_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(organization, MOCK_ORGANIZATION_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Organization/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_patient(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PATIENT
        assert mock_auth.return_value == None
        patient = get_patient()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(patient, MOCK_PATIENT)
        mock_get.assert_called_once_with(
            self.health_url + "Patient",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "_id": None,
                "identifier": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_patient_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PATIENT_ID
        assert mock_auth.return_value == None
        mock_id = "I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000"
        patient = get_patient_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(patient, MOCK_PATIENT_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Patient/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_practitioner(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PRACTITIONER
        assert mock_auth.return_value == None
        practitioner = get_practitioner()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(practitioner, MOCK_PRACTITIONER)
        mock_get.assert_called_once_with(
            self.health_url + "Practitioner",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "_id": None,
                "identifier": None,
                "family": None,
                "given": None,
                "name": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_practioner_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PRACTITIONER_ID
        assert mock_auth.return_value == None
        mock_id = "I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000"
        practitioner = get_practitioner_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(practitioner, MOCK_PRACTITIONER_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Practitioner/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_practitioner_role(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PRACTITIONER_ROLE
        assert mock_auth.return_value == None
        practitioner_role = get_practitioner_role()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(practitioner_role, MOCK_PRACTITIONER_ROLE)
        mock_get.assert_called_once_with(
            self.health_url + "PractitionerRole",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "_id": None,
                "identifier": None,
                "name": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_practioner_role_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PRACTITIONER_ROLE_ID
        assert mock_auth.return_value == None
        mock_id = "I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000"
        practitioner_role = get_practitioner_role_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(practitioner_role, MOCK_PRACTITIONER_ROLE_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"PractitionerRole/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_procedure(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PROCEDURE
        assert mock_auth.return_value == None
        procedure = get_procedure()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(procedure, MOCK_PROCEDURE)
        mock_get.assert_called_once_with(
            self.health_url + "Procedure",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
            params={
                "patient": None,
                "_id": None,
                "identifier": None,
                "date": None,
                "_lastUpdated": None,
                "page": 1,
                "_count": 30,
            },
        )

    def test_get_procedure_by_id(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_PROCEDURE_ID
        assert mock_auth.return_value == None
        mock_id = "I2-TD6AZ3E7TO2DYFFXQOIWZNC3FM000000"
        procedure = get_procedure_by_id(mock_id)
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(procedure, MOCK_PROCEDURE_ID)
        mock_get.assert_called_once_with(
            self.health_url + f"Procedure/{mock_id}",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )

    def test_get_metadata(self, mock_get, mock_auth, mock_token):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_METADATA
        assert mock_auth.return_value == None
        metadata = get_metadata()
        mock_token.assert_called_once()
        assert mock_token.return_value == "somerandomtoken"
        assert mock_get.headers == self.headers
        self.assertDictEqual(metadata, MOCK_METADATA)
        mock_get.assert_called_once_with(
            self.health_url + "metadata",
            headers=dict(
                apiKey=creds.API_KEY_HEADER.get("apiKey"),
                Authorization="Bearer somerandomtoken",
            ),
        )


if __name__ == "__main__":
    unittest.main()

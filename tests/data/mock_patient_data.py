MOCK_ALLERGY_INTOLERANCE = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 15,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/AllergyIntolerance?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/AllergyIntolerance?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/AllergyIntolerance?patient=43000199&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/AllergyIntolerance?patient=43000199&_count=1&page=15",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/AllergyIntolerance/I2-FY4N5GUAQ4IZQVQZUPDFN43S4A000000",
            "resource": {
                "resourceType": "AllergyIntolerance",
                "id": "I2-FY4N5GUAQ4IZQVQZUPDFN43S4A000000",
                "clinicalStatus": {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/ValueSet/allergyintolerance-clinical",
                            "code": "active",
                        }
                    ]
                },
                "type": "allergy",
                "code": {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "300916003",
                            "display": "Latex allergy",
                        }
                    ],
                    "text": "Latex allergy",
                },
                "patient": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
                    "display": "Ms. Carlita746 Kautzer186",
                },
                "recordedDate": "1999-01-07T01:43:31Z",
                "recorder": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-4ZXYC2SQAZCHMOWPPFNLOY65GE000000",
                    "display": "DR. THOMAS359 REYNOLDS206 PHD",
                },
                "note": [
                    {
                        "authorReference": {
                            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
                            "display": "DR. JANE460 DOE922 MD",
                        },
                        "time": "1999-01-07T01:43:31Z",
                        "text": "Latex allergy",
                    }
                ],
                "reaction": [
                    {
                        "substance": {
                            "coding": [
                                {
                                    "system": "http://snomed.info/sct",
                                    "code": "300916003",
                                    "display": "Latex allergy",
                                }
                            ],
                            "text": "Latex allergy",
                        },
                        "manifestation": [
                            {
                                "coding": [
                                    {
                                        "system": "urn:oid:2.16.840.1.113883.6.233",
                                        "code": "43000006",
                                        "display": "Itchy Watery Eyes",
                                    }
                                ],
                                "text": "Itchy Watery Eyes",
                            }
                        ],
                    }
                ],
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_ALLERGY_INTOLERANCE_ID = {
    "resourceType": "AllergyIntolerance",
    "id": "I2-FY4N5GUAQ4IZQVQZUPDFN43S4A000000",
    "clinicalStatus": {
        "coding": [
            {
                "system": "http://hl7.org/fhir/ValueSet/allergyintolerance-clinical",
                "code": "active",
            }
        ]
    },
    "type": "allergy",
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "300916003",
                "display": "Latex allergy",
            }
        ],
        "text": "Latex allergy",
    },
    "patient": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
        "display": "Ms. Carlita746 Kautzer186",
    },
    "recordedDate": "1999-01-07T01:43:31Z",
    "recorder": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-4ZXYC2SQAZCHMOWPPFNLOY65GE000000",
        "display": "DR. THOMAS359 REYNOLDS206 PHD",
    },
    "note": [
        {
            "authorReference": {
                "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
                "display": "DR. JANE460 DOE922 MD",
            },
            "time": "1999-01-07T01:43:31Z",
            "text": "Latex allergy",
        }
    ],
    "reaction": [
        {
            "substance": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "300916003",
                        "display": "Latex allergy",
                    }
                ],
                "text": "Latex allergy",
            },
            "manifestation": [
                {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.233",
                            "code": "43000006",
                            "display": "Itchy Watery Eyes",
                        }
                    ],
                    "text": "Itchy Watery Eyes",
                }
            ],
        }
    ],
}

MOCK_APPOINTMENT = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 3,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Appointment?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Appointment?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Appointment?patient=43000199&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Appointment?patient=43000199&_count=1&page=3",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Appointment/I2-V7QE6HNG7MXDOIEWC534Y3HRYWKJGRCGJSVDZW7YDHXR7RMD2FWA0000",
            "resource": {
                "resourceType": "Appointment",
                "id": "I2-V7QE6HNG7MXDOIEWC534Y3HRYWKJGRCGJSVDZW7YDHXR7RMD2FWA0000",  # pragma: allowlist secret
                "meta": {"lastUpdated": "2020-11-01T12:30:00Z"},
                "status": "cancelled",
                "cancelationReason": {
                    "coding": [
                        {
                            "system": "http://www.va.gov/Terminology/VistADefinedTerms/2.98-16",
                            "display": "SCHEDULING CONFLICT/ERROR",
                        }
                    ],
                    "text": "SCHEDULING CONFLICT/ERROR",
                },
                "serviceCategory": [
                    {
                        "coding": [
                            {
                                "system": "http://www.va.gov/Terminology/VistADefinedTerms/44-9",
                                "code": "M",
                                "display": "MEDICINE",
                            }
                        ],
                        "text": "MEDICINE",
                    }
                ],
                "serviceType": [{"text": "CARDIOLOGY"}],
                "description": "Scheduled Visit",
                "start": "2020-10-02T12:00:00Z",
                "end": "2020-10-02T12:30:00Z",
                "minutesDuration": 30,
                "created": "2020-09-16",
                "participant": [
                    {
                        "actor": {
                            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                            "display": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
                        },
                        "status": "accepted",
                    },
                    {
                        "actor": {
                            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
                            "display": "Kautzer186, Carlita746",
                        },
                        "status": "accepted",
                    },
                ],
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_APPOINTMENT_ID = {
    "resourceType": "Appointment",
    "id": "I2-V7QE6HNG7MXDOIEWC534Y3HRYWKJGRCGJSVDZW7YDHXR7RMD2FWA0000",  # pragma: allowlist secret
    "meta": {"lastUpdated": "2020-11-01T12:30:00Z"},
    "status": "cancelled",
    "cancelationReason": {
        "coding": [
            {
                "system": "http://www.va.gov/Terminology/VistADefinedTerms/2.98-16",
                "display": "SCHEDULING CONFLICT/ERROR",
            }
        ],
        "text": "SCHEDULING CONFLICT/ERROR",
    },
    "serviceCategory": [
        {
            "coding": [
                {
                    "system": "http://www.va.gov/Terminology/VistADefinedTerms/44-9",
                    "code": "M",
                    "display": "MEDICINE",
                }
            ],
            "text": "MEDICINE",
        }
    ],
    "serviceType": [{"text": "CARDIOLOGY"}],
    "description": "Scheduled Visit",
    "start": "2020-10-02T12:00:00Z",
    "end": "2020-10-02T12:30:00Z",
    "minutesDuration": 30,
    "created": "2020-09-16",
    "participant": [
        {
            "actor": {
                "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "display": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
            },
            "status": "accepted",
        },
        {
            "actor": {
                "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
                "display": "Kautzer186, Carlita746",
            },
            "status": "accepted",
        },
    ],
}

MOCK_BINARY_ID = {
    "resourceType": "Binary",
    "id": "4-10cM2Q9dqjfi52cS61pfSBhDWrpLiQiSAJ4MGNtHN",  # pragma: allowlist secret
    "contentType": "text/plain",
    "securityContext": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1011537977V693883"
    },
    "data": "VGhpcyBwYXRpZW50IGhhcyBoYWQgdGhlIGZvbGxvd2luZyByZWFjdGlvbnMKc2lnbmVkLW9mZiBvbiBKdWwgMjQsIDIwMjBAMDg6NTg6NDYuCgpQRUFOVVRTCgpBdXRob3IncyBjb21tZW50czoKCkNvbW1lbnQgTGluZSAxIENvbW1lbnQgTGluZSAyIENvbW1lbnQgTGluZSAzIENvbW1lbnQgTGluZSA0CkNvbW1lbnQgTGluZSA0IENvbW1lbnQgTGluZSA1IENvbW1lbnQgTGluZSA2IENvbW1lbnQgTGluZSA3CkNvbW1lbnQgTGluZSA4IENvbW1lbnQgTGluZSA5IENvbW1lbnQgTGluZSAxMCBDb21tZW50IExpbmUKMTEgQ29tbWVudCBMaW5lIDEyIENvbW1lbnQgTGluZSAxMyBDb21tZW50IExpbmUgMTQgQ29tbWVudApMaW5lIDE1IENvbW1lbnQgTGluZSAxNiBDb21tZW50IExpbmUgMTcgQ29tbWVudCBMaW5lIDE4CkNvbW1lbnQgTGluZSAxOSBDb21tZW50IExpbmUgMjAKCgoKCg==",  # pragma: allowlist secret
}

MOCK_CONDITION = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 12,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Condition?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Condition?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Condition?patient=43000199&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Condition?patient=43000199&_count=1&page=12",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Condition/I2-TWYEPQNF7H5A4OG5P3SW55FP44000000",
            "resource": {
                "resourceType": "Condition",
                "id": "I2-TWYEPQNF7H5A4OG5P3SW55FP44000000",
                "clinicalStatus": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                            "code": "active",
                            "display": "Active",
                        }
                    ],
                    "text": "Active",
                },
                "verificationStatus": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                            "code": "confirmed",
                            "display": "Confirmed",
                        }
                    ],
                    "text": "Confirmed",
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/condition-category",
                                "code": "encounter-diagnosis",
                                "display": "Encounter Diagnosis",
                            }
                        ],
                        "text": "Encounter Diagnosis",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "40055000",
                            "display": "Chronic sinusitis (disorder)",
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "J01.21",
                            "display": "Acute recurrent ethmoidal sinusitis",
                        },
                    ],
                    "text": "Chronic sinusitis (disorder)",
                },
                "subject": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
                    "display": "Ms. Carlita746 Kautzer186",
                },
                "onsetDateTime": "1998-12-28T01:43:31Z",
                "recordedDate": "1998-12-27",
                "recorder": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-QXZOEMHBZNNC7BUGOTHVWYSZAI000000",
                    "display": "DR. JOHN248 SMITH811 MD",
                },
                "asserter": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-QXZOEMHBZNNC7BUGOTHVWYSZAI000000",
                    "display": "DR. JOHN248 SMITH811 MD",
                },
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_CONDITION_ID = {
    "resourceType": "Condition",
    "id": "I2-TWYEPQNF7H5A4OG5P3SW55FP44000000",
    "clinicalStatus": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                "code": "active",
                "display": "Active",
            }
        ],
        "text": "Active",
    },
    "verificationStatus": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                "code": "confirmed",
                "display": "Confirmed",
            }
        ],
        "text": "Confirmed",
    },
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/condition-category",
                    "code": "encounter-diagnosis",
                    "display": "Encounter Diagnosis",
                }
            ],
            "text": "Encounter Diagnosis",
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "40055000",
                "display": "Chronic sinusitis (disorder)",
            },
            {
                "system": "http://hl7.org/fhir/sid/icd-10-cm",
                "code": "J01.21",
                "display": "Acute recurrent ethmoidal sinusitis",
            },
        ],
        "text": "Chronic sinusitis (disorder)",
    },
    "subject": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
        "display": "Ms. Carlita746 Kautzer186",
    },
    "onsetDateTime": "1998-12-28T01:43:31Z",
    "recordedDate": "1998-12-27",
    "recorder": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-QXZOEMHBZNNC7BUGOTHVWYSZAI000000",
        "display": "DR. JOHN248 SMITH811 MD",
    },
    "asserter": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-QXZOEMHBZNNC7BUGOTHVWYSZAI000000",
        "display": "DR. JOHN248 SMITH811 MD",
    },
}

MOCK_DEVICE = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 2,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Device?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Device?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Device?patient=43000199&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Device?patient=43000199&_count=1&page=2",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Device/I2-DPWVDPSF36SDG527A43QRGHKUU5G2VYK5KITXOWUDY222Q5ZOJJQ0000",
            "resource": {
                "resourceType": "Device",
                "id": "I2-DPWVDPSF36SDG527A43QRGHKUU5G2VYK5KITXOWUDY222Q5ZOJJQ0000",  # pragma: allowlist secret
                "manufacturer": "BOSTON SCIENTIFIC",
                "lotNumber": "J12095",
                "serialNumber": "152906",
                "deviceName": [
                    {"name": "L664", "type": "model-name"},
                    {"name": "EYEGLASSES", "type": "user-friendly-name"},
                ],
                "type": {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "257193001",
                            "display": "Telescopic eyeglasses",
                        }
                    ],
                    "text": "Telescopic eyeglasses",
                },
                "patient": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
                    "display": "Kautzer186, Carlita746",
                },
                "owner": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                    "display": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
                },
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_DEVICE_ID = {
    "resourceType": "Device",
    "id": "I2-DPWVDPSF36SDG527A43QRGHKUU5G2VYK5KITXOWUDY222Q5ZOJJQ0000",  # pragma: allowlist secret
    "manufacturer": "BOSTON SCIENTIFIC",
    "lotNumber": "J12095",
    "serialNumber": "152906",
    "deviceName": [
        {"name": "L664", "type": "model-name"},
        {"name": "EYEGLASSES", "type": "user-friendly-name"},
    ],
    "type": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "257193001",
                "display": "Telescopic eyeglasses",
            }
        ],
        "text": "Telescopic eyeglasses",
    },
    "patient": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
        "display": "Kautzer186, Carlita746",
    },
    "owner": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
        "display": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
    },
}

MOCK_DEVICE_REQUEST = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DeviceRequest?patient=1017283148V813263&page=1&_count=15",
        },
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DeviceRequest?patient=1017283148V813263&page=1&_count=15",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DeviceRequest?patient=1017283148V813263&page=1&_count=15",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/DeviceRequest/I2-UFT532RWEIOS2WWZQWXUB7TKCT5SODPVTQJQD3ZNZUSAXXB4KZXQ0000",
            "resource": {
                "resourceType": "DeviceRequest",
                "id": "I2-UFT532RWEIOS2WWZQWXUB7TKCT5SODPVTQJQD3ZNZUSAXXB4KZXQ0000",  # pragma: allowlist secret
                "meta": {"lastUpdated": "2021-12-01T00:00:00Z"},
                "status": "completed",
                "intent": "order",
                "codeCodeableConcept": {"text": "PROSTHETICS REQUEST - CPAP/BIPAP"},
                "subject": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1017283148V813263",
                    "display": "Mr. Aurelio227 Cruickshank494",
                },
                "occurrenceDateTime": "2009-12-30T22:27:00Z",
                "requester": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
                    "display": "DR. JANE460 DOE922 MD",
                },
                "reasonCode": [
                    {
                        "coding": [
                            {
                                "system": "http://hl7.org/fhir/sid/icd-10-cm",
                                "version": "10",
                                "code": "G47.30",
                                "display": "Sleep apnea, unspecified",
                            }
                        ],
                        "text": "Sleep apnea, unspecified",
                    }
                ],
            },
        }
    ],
}

MOCK_DEVICE_REQUEST_ID = {
    "resourceType": "DeviceRequest",
    "id": "I2-UFT532RWEIOS2WWZQWXUB7TKCT5SODPVTQJQD3ZNZUSAXXB4KZXQ0000",  # pragma: allowlist secret
    "meta": {"lastUpdated": "2021-12-01T00:00:00Z"},
    "status": "completed",
    "intent": "order",
    "codeCodeableConcept": {"text": "PROSTHETICS REQUEST - CPAP/BIPAP"},
    "subject": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1017283148V813263",
        "display": "Mr. Aurelio227 Cruickshank494",
    },
    "occurrenceDateTime": "2009-12-30T22:27:00Z",
    "requester": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
        "display": "DR. JANE460 DOE922 MD",
    },
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/sid/icd-10-cm",
                    "version": "10",
                    "code": "G47.30",
                    "display": "Sleep apnea, unspecified",
                }
            ],
            "text": "Sleep apnea, unspecified",
        }
    ],
}

MOCK_DIAGNOSTIC_REPORT = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 22,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DiagnosticReport?patient=1000005&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DiagnosticReport?patient=1000005&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DiagnosticReport?patient=1000005&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DiagnosticReport?patient=1000005&_count=1&page=22",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/DiagnosticReport/I2-EWSRFHMJRWT3KNBUB542ZJYEKM000000",
            "resource": {
                "resourceType": "DiagnosticReport",
                "id": "I2-EWSRFHMJRWT3KNBUB542ZJYEKM000000",
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                                "code": "LAB",
                                "display": "Laboratory",
                            }
                        ],
                        "text": "Laboratory",
                    }
                ],
                "code": {"text": "panel"},
                "subject": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1000005",
                    "display": "Mr. Shane235 Bartell116",
                },
                "effectiveDateTime": "1998-03-16T05:56:37Z",
                "issued": "1998-03-16T05:56:37Z",
                "result": [
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000",
                        "display": "Glucose",
                    },
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-6DTSU5DDGS3NBDOKN4BOZDISGE000000",
                        "display": "Urea Nitrogen",
                    },
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-4OWFD25REFR6P362ZJ2PY3ACWU000000",
                        "display": "Creatinine",
                    },
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-35GNQKPTBRNMPBTUGEF4F62HNI000000",
                        "display": "Calcium",
                    },
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-OOVHBIQFYCOORXPBB74H42FPJU000000",
                        "display": "Sodium",
                    },
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-C3P7YCD3DCX7KNRRR5DOKLDCGA000000",
                        "display": "Potassium",
                    },
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-K4NGUOCHCS3ULYOFMDN5ZRJW6U000000",
                        "display": "Chloride",
                    },
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-D5TBNWZQSFRRBOBSBCC7QQRPQY000000",
                        "display": "Carbon Dioxide",
                    },
                ],
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_DIAGNOSTIC_REPORT_ID = {
    "resourceType": "DiagnosticReport",
    "id": "I2-EWSRFHMJRWT3KNBUB542ZJYEKM000000",
    "status": "final",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                    "code": "LAB",
                    "display": "Laboratory",
                }
            ],
            "text": "Laboratory",
        }
    ],
    "code": {"text": "panel"},
    "subject": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1000005",
        "display": "Mr. Shane235 Bartell116",
    },
    "effectiveDateTime": "1998-03-16T05:56:37Z",
    "issued": "1998-03-16T05:56:37Z",
    "result": [
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000",
            "display": "Glucose",
        },
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-6DTSU5DDGS3NBDOKN4BOZDISGE000000",
            "display": "Urea Nitrogen",
        },
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-4OWFD25REFR6P362ZJ2PY3ACWU000000",
            "display": "Creatinine",
        },
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-35GNQKPTBRNMPBTUGEF4F62HNI000000",
            "display": "Calcium",
        },
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-OOVHBIQFYCOORXPBB74H42FPJU000000",
            "display": "Sodium",
        },
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-C3P7YCD3DCX7KNRRR5DOKLDCGA000000",
            "display": "Potassium",
        },
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-K4NGUOCHCS3ULYOFMDN5ZRJW6U000000",
            "display": "Chloride",
        },
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-D5TBNWZQSFRRBOBSBCC7QQRPQY000000",
            "display": "Carbon Dioxide",
        },
    ],
}

MOCK_DOCUMENT_REFERENCE = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 8,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DocumentReference?patient=1011537977V693883&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DocumentReference?patient=1011537977V693883&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DocumentReference?patient=1011537977V693883&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/DocumentReference?patient=1011537977V693883&_count=1&page=8",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/DocumentReference/I2-3B2LP2KAI3TVQEB6EGKVZZKBVT5VOZPOMH2WZMEG3BUU7IDDRFYA0000",
            "resource": {
                "resourceType": "DocumentReference",
                "id": "I2-3B2LP2KAI3TVQEB6EGKVZZKBVT5VOZPOMH2WZMEG3BUU7IDDRFYA0000",  # pragma: allowlist secret
                "meta": {"lastUpdated": "2021-11-29T16:30:06Z"},
                "status": "current",
                "docStatus": "final",
                "type": {
                    "coding": [
                        {
                            "system": "http://loinc.org",
                            "code": "68629-5",
                            "display": "NOTE",
                        }
                    ],
                    "text": "NOTE",
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-category",
                                "display": "clinical-note",
                            }
                        ],
                        "text": "clinical-note",
                    }
                ],
                "subject": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1011537977V693883",
                    "display": "Ms. Carlita746 Kautzer186",
                },
                "date": "2021-11-29T16:30:06Z",
                "author": [
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-QXZOEMHBZNNC7BUGOTHVWYSZAI000000",
                        "display": "DR. JOHN248 SMITH811 MD",
                    }
                ],
                "custodian": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-TNGGKEZYBO7Y56PQ3WWK5KTOSM000000",
                    "display": "MINNEAPOLIS VAMC",
                },
                "content": [
                    {
                        "attachment": {
                            "id": "4943723",
                            "contentType": "text/plain",
                            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Binary/4-10cM2Q9dqjfi52cS61pfSBhDWrpLiQiSAJ4MGNtHN",
                            "title": "ALLERGY & IMMUNOLOGY NOTE",
                            "creation": "2021-11-29T16:30:06Z",
                        }
                    }
                ],
                "context": {
                    "encounter": [
                        {
                            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Encounter/I2-5WR43OIGY4625GCVOZTBYODWIEVVWLDDWEDSXUTTHZCTHKKBIDTQ0000"
                        }
                    ],
                    "period": {"start": "2021-11-29T16:30:06Z"},
                    "facilityType": {
                        "coding": [
                            {
                                "system": "http://hl7.org/fhir/ValueSet/c80-facilitycodes",
                                "display": "CLINIC",
                            }
                        ],
                        "text": "CLINIC",
                    },
                },
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_DOCUMENT_REFERENCE_ID = {
    "resourceType": "DocumentReference",
    "id": "I2-3B2LP2KAI3TVQEB6EGKVZZKBVT5VOZPOMH2WZMEG3BUU7IDDRFYA0000",  # pragma: allowlist secret
    "meta": {"lastUpdated": "2021-11-29T16:30:06Z"},
    "status": "current",
    "docStatus": "final",
    "type": {
        "coding": [
            {"system": "http://loinc.org", "code": "68629-5", "display": "NOTE"}
        ],
        "text": "NOTE",
    },
    "category": [
        {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-category",
                    "display": "clinical-note",
                }
            ],
            "text": "clinical-note",
        }
    ],
    "subject": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1011537977V693883",
        "display": "Ms. Carlita746 Kautzer186",
    },
    "date": "2021-11-29T16:30:06Z",
    "author": [
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-QXZOEMHBZNNC7BUGOTHVWYSZAI000000",
            "display": "DR. JOHN248 SMITH811 MD",
        }
    ],
    "custodian": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-TNGGKEZYBO7Y56PQ3WWK5KTOSM000000",
        "display": "MINNEAPOLIS VAMC",
    },
    "content": [
        {
            "attachment": {
                "id": "4943723",
                "contentType": "text/plain",
                "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Binary/4-10cM2Q9dqjfi52cS61pfSBhDWrpLiQiSAJ4MGNtHN",
                "title": "ALLERGY & IMMUNOLOGY NOTE",
                "creation": "2021-11-29T16:30:06Z",
            }
        }
    ],
    "context": {
        "encounter": [
            {
                "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Encounter/I2-5WR43OIGY4625GCVOZTBYODWIEVVWLDDWEDSXUTTHZCTHKKBIDTQ0000"
            }
        ],
        "period": {"start": "2021-11-29T16:30:06Z"},
        "facilityType": {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/ValueSet/c80-facilitycodes",
                    "display": "CLINIC",
                }
            ],
            "text": "CLINIC",
        },
    },
}

MOCK_ENCOUNTER = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 2,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Encounter?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Encounter?patient=43000199&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Encounter?patient=43000199&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Encounter?patient=43000199&_count=1&page=2",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Encounter/I2-5WR43OIGY4625GCVOZTBYODWIEVVWLDDWEDSXUTTHZCTHKKBIDTQ0000",
            "resource": {
                "resourceType": "Encounter",
                "id": "I2-5WR43OIGY4625GCVOZTBYODWIEVVWLDDWEDSXUTTHZCTHKKBIDTQ0000",  # pragma: allowlist secret
                "meta": {"lastUpdated": "2021-12-01T00:00:00Z"},
                "status": "finished",
                "type": [
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "36556",
                                "display": "INSERT NON-TUNNEL CV CATH",
                            }
                        ],
                        "text": "INSERTION OF NON-TUNNELED CENTRALLY INSERTED CENTRAL VENOUS CATHETER; AGE 5 YEARS OR OLDER",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "71045",
                                "display": "X-RAY EXAM CHEST 1 VIEW",
                            }
                        ],
                        "text": "RADIOLOGIC EXAMINATION, CHEST; SINGLE VIEW",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "74018",
                                "display": "X-RAY EXAM ABDOMEN 1 VIEW",
                            }
                        ],
                        "text": "RADIOLOGIC EXAMINATION, ABDOMEN; 1 VIEW",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "76937",
                                "display": "US GUIDE VASCULAR ACCESS",
                            }
                        ],
                        "text": "ULTRASOUND GUIDANCE FOR VASCULAR ACCESS REQUIRING ULTRASOUND EVALUATION OF POTENTIAL ACCESS SITES, DOCUMENTATION OF SELECTED VESSEL PATENCY, CONCURRENT REALTIME ULTRASOUND VISUALIZATION OF VASCULAR NEEDLE ENTRY, WITH PERMANENT RECORDING AND REPORTING (LIST SEPARATELY IN ADDITION TO CODE FOR PRIMARY PROCEDURE)",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "97129",
                                "display": "THER IVNTJ 1ST 15 MIN",
                            }
                        ],
                        "text": "THERAPEUTIC INTERVENTIONS THAT FOCUS ON COGNITIVE FUNCTION (EG, ATTENTION, MEMORY, REASONING, EXECUTIVE FUNCTION, PROBLEM SOLVING, AND/OR PRAGMATIC FUNCTIONING) AND COMPENSATORY STRATEGIES TO MANAGE THE PERFORMANCE OF AN ACTIVITY (EG, MANAGING TIME OR SCHEDULES, INITIATING, ORGANIZING, AND SEQUENCING TASKS), DIRECT (ONE-ON-ONE) PATIENT CONTACT; INITIAL 15 MINUTES",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "97161",
                                "display": "PT EVAL LOW COMPLEX 20 MIN",
                            }
                        ],
                        "text": "PHYSICAL THERAPY EVALUATION: LOW COMPLEXITY, REQUIRING THESE COMPONENTS: A HISTORY WITH NO PERSONAL FACTORS AND/OR COMORBIDITIES THAT IMPACT THE PLAN OF CARE; AN EXAMINATION OF BODY SYSTEM(S) USING STANDARDIZED TESTS AND MEASURES ADDRESSING 1-2 ELEMENTS FROM ANY OF THE FOLLOWING: BODY STRUCTURES AND FUNCTIONS, ACTIVITY LIMITATIONS, AND/OR PARTICIPATION RESTRICTIONS; A CLINICAL PRESENTATION WITH STABLE AND/OR UNCOMPLICATED CHARACTERISTICS; AND CLINICAL DECISION MAKING OF LOW COMPLEXITY USING STANDARDIZED PATIENT ASSESSMENT INSTRUMENT AND/OR MEASURABLE ASSESSMENT OF FUNCTIONAL OUTCOME. TYPICALLY, 20 MINUTES ARE SPENT FACE-TO-FACE WITH THE PATIENT AND/OR FAMILY.",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "97165",
                                "display": "OT EVAL LOW COMPLEX 30 MIN",
                            }
                        ],
                        "text": "OCCUPATIONAL THERAPY EVALUATION, LOW COMPLEXITY, REQUIRING THESE COMPONENTS: AN OCCUPATIONAL PROFILE AND MEDICAL AND THERAPY HISTORY, WHICH INCLUDES A BRIEF HISTORY INCLUDING REVIEW OF MEDICAL AND/OR THERAPY RECORDS RELATING TO THE PRESENTING PROBLEM; AN ASSESSMENT(S) THAT IDENTIFIES 1-3 PERFORMANCE DEFICITS (IE, RELATING TO PHYSICAL, COGNITIVE, OR PSYCHOSOCIAL SKILLS) THAT RESULT IN ACTIVITY LIMITATIONS AND/OR PARTICIPATION RESTRICTIONS; AND CLINICAL DECISION MAKING OF LOW COMPLEXITY, WHICH INCLUDES AN ANALYSIS OF THE OCCUPATIONAL PROFILE, ANALYSIS OF DATA FROM PROBLEM-FOCUSED ASSESSMENT(S), AND CONSIDERATION OF A LIMITED NUMBER OF TREATMENT OPTIONS. PATIENT PRESENTS WITH NO COMORBIDITIES THAT AFFECT OCCUPATIONAL PERFORMANCE. MODIFICATION OF TASKS OR ASSISTANCE (EG, PHYSICAL OR VERBAL) WITH ASSESSMENT(S) IS NOT NECESSARY TO ENABLE COMPLETION OF EVALUATION COMPONENT. TYPICALLY, 30 MINUTES ARE SPENT FACE-TO-FACE WITH THE PATIENT AND/OR FAMILY.",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "97530",
                                "display": "THERAPEUTIC ACTIVITIES",
                            }
                        ],
                        "text": "THERAPEUTIC ACTIVITIES, DIRECT (ONE-ON-ONE) PATIENT CONTACT (USE OF DYNAMIC ACTIVITIES TO IMPROVE FUNCTIONAL PERFORMANCE), EACH 15 MINUTES",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "99213",
                                "display": "OFFICE O/P EST LOW 20-29 MIN",
                            }
                        ],
                        "text": "OFFICE OR OTHER OUTPATIENT VISIT FOR THE EVALUATION AND MANAGEMENT OF AN ESTABLISHED PATIENT, WHICH REQUIRES A MEDICALLY APPROPRIATE HISTORY AND/OR EXAMINATION AND LOW LEVEL OF MEDICAL DECISION MAKING. WHEN USING TIME FOR CODE SELECTION, 20-29 MINUTES OF TOTAL TIME IS SPENT ON THE DATE OF THE ENCOUNTER.",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "99222",
                                "display": "INITIAL HOSPITAL CARE",
                            }
                        ],
                        "text": "INITIAL HOSPITAL CARE, PER DAY, FOR THE EVALUATION AND MANAGEMENT OF A PATIENT, WHICH REQUIRES THESE 3 KEY COMPONENTS: A COMPREHENSIVE HISTORY; A COMPREHENSIVE EXAMINATION; AND MEDICAL DECISION MAKING OF MODERATE COMPLEXITY. COUNSELING AND/OR COORDINATION OF CARE WITH OTHER PHYSICIANS, OTHER QUALIFIED HEALTH CARE PROFESSIONALS, OR AGENCIES ARE PROVIDED CONSISTENT WITH THE NATURE OF THE PROBLEM(S) AND THE PATIENT'S AND/OR FAMILY'S NEEDS. USUALLY, THE PROBLEM(S) REQUIRING ADMISSION ARE OF MODERATE SEVERITY. TYPICALLY, 50 MINUTES ARE SPENT AT THE BEDSIDE AND ON THE PATIENT'S HOSPITAL FLOOR OR UNIT.",
                    },
                    {
                        "coding": [
                            {
                                "system": "http://www.ama-assn.org/go/cpt",
                                "code": "99238",
                                "display": "HOSPITAL DISCHARGE DAY",
                            }
                        ],
                        "text": "HOSPITAL DISCHARGE DAY MANAGEMENT; 30 MINUTES OR LESS",
                    },
                ],
                "serviceType": {"text": "inpatient"},
                "subject": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
                    "display": "Ms. Carlita746 Kautzer186",
                },
                "period": {"start": "2021-11-29", "end": "2021-12-01"},
                "reasonCode": [
                    {
                        "coding": [
                            {
                                "system": "http://www.va.gov/Terminology/VistADefinedTerms/9000010-.07",
                                "version": "9",
                                "code": "780.4",
                                "display": "DIZZINESS AND GIDDINESS",
                            }
                        ],
                        "text": "DIZZINESS AND GIDDINESS",
                    }
                ],
                "hospitalization": {
                    "dischargeDisposition": {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/discharge-disposition",
                                "code": "X",
                                "display": "RETURN TO COMMUNITY-INDEPENDENT",
                            }
                        ],
                        "text": "RETURN TO COMMUNITY-INDEPENDENT",
                    }
                },
                "location": [
                    {
                        "location": {
                            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-2FPCKUIXVR7RJLLG34XVWGZERM000000",
                            "display": "MENTAL HEALTH SERVICES",
                        }
                    }
                ],
                "serviceProvider": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-YCRI7L52BYQL63ZFALGWIWF2WU000000",
                    "display": "WASHINGTON VA MEDICAL CENTER",
                },
                "class": {"display": "IMP"},
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_ENCOUNTER_ID = {
    "resourceType": "Encounter",
    "id": "I2-5WR43OIGY4625GCVOZTBYODWIEVVWLDDWEDSXUTTHZCTHKKBIDTQ0000",  # pragma: allowlist secret
    "meta": {"lastUpdated": "2021-12-01T00:00:00Z"},
    "status": "finished",
    "type": [
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "36556",
                    "display": "INSERT NON-TUNNEL CV CATH",
                }
            ],
            "text": "INSERTION OF NON-TUNNELED CENTRALLY INSERTED CENTRAL VENOUS CATHETER; AGE 5 YEARS OR OLDER",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "71045",
                    "display": "X-RAY EXAM CHEST 1 VIEW",
                }
            ],
            "text": "RADIOLOGIC EXAMINATION, CHEST; SINGLE VIEW",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "74018",
                    "display": "X-RAY EXAM ABDOMEN 1 VIEW",
                }
            ],
            "text": "RADIOLOGIC EXAMINATION, ABDOMEN; 1 VIEW",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "76937",
                    "display": "US GUIDE VASCULAR ACCESS",
                }
            ],
            "text": "ULTRASOUND GUIDANCE FOR VASCULAR ACCESS REQUIRING ULTRASOUND EVALUATION OF POTENTIAL ACCESS SITES, DOCUMENTATION OF SELECTED VESSEL PATENCY, CONCURRENT REALTIME ULTRASOUND VISUALIZATION OF VASCULAR NEEDLE ENTRY, WITH PERMANENT RECORDING AND REPORTING (LIST SEPARATELY IN ADDITION TO CODE FOR PRIMARY PROCEDURE)",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "97129",
                    "display": "THER IVNTJ 1ST 15 MIN",
                }
            ],
            "text": "THERAPEUTIC INTERVENTIONS THAT FOCUS ON COGNITIVE FUNCTION (EG, ATTENTION, MEMORY, REASONING, EXECUTIVE FUNCTION, PROBLEM SOLVING, AND/OR PRAGMATIC FUNCTIONING) AND COMPENSATORY STRATEGIES TO MANAGE THE PERFORMANCE OF AN ACTIVITY (EG, MANAGING TIME OR SCHEDULES, INITIATING, ORGANIZING, AND SEQUENCING TASKS), DIRECT (ONE-ON-ONE) PATIENT CONTACT; INITIAL 15 MINUTES",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "97161",
                    "display": "PT EVAL LOW COMPLEX 20 MIN",
                }
            ],
            "text": "PHYSICAL THERAPY EVALUATION: LOW COMPLEXITY, REQUIRING THESE COMPONENTS: A HISTORY WITH NO PERSONAL FACTORS AND/OR COMORBIDITIES THAT IMPACT THE PLAN OF CARE; AN EXAMINATION OF BODY SYSTEM(S) USING STANDARDIZED TESTS AND MEASURES ADDRESSING 1-2 ELEMENTS FROM ANY OF THE FOLLOWING: BODY STRUCTURES AND FUNCTIONS, ACTIVITY LIMITATIONS, AND/OR PARTICIPATION RESTRICTIONS; A CLINICAL PRESENTATION WITH STABLE AND/OR UNCOMPLICATED CHARACTERISTICS; AND CLINICAL DECISION MAKING OF LOW COMPLEXITY USING STANDARDIZED PATIENT ASSESSMENT INSTRUMENT AND/OR MEASURABLE ASSESSMENT OF FUNCTIONAL OUTCOME. TYPICALLY, 20 MINUTES ARE SPENT FACE-TO-FACE WITH THE PATIENT AND/OR FAMILY.",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "97165",
                    "display": "OT EVAL LOW COMPLEX 30 MIN",
                }
            ],
            "text": "OCCUPATIONAL THERAPY EVALUATION, LOW COMPLEXITY, REQUIRING THESE COMPONENTS: AN OCCUPATIONAL PROFILE AND MEDICAL AND THERAPY HISTORY, WHICH INCLUDES A BRIEF HISTORY INCLUDING REVIEW OF MEDICAL AND/OR THERAPY RECORDS RELATING TO THE PRESENTING PROBLEM; AN ASSESSMENT(S) THAT IDENTIFIES 1-3 PERFORMANCE DEFICITS (IE, RELATING TO PHYSICAL, COGNITIVE, OR PSYCHOSOCIAL SKILLS) THAT RESULT IN ACTIVITY LIMITATIONS AND/OR PARTICIPATION RESTRICTIONS; AND CLINICAL DECISION MAKING OF LOW COMPLEXITY, WHICH INCLUDES AN ANALYSIS OF THE OCCUPATIONAL PROFILE, ANALYSIS OF DATA FROM PROBLEM-FOCUSED ASSESSMENT(S), AND CONSIDERATION OF A LIMITED NUMBER OF TREATMENT OPTIONS. PATIENT PRESENTS WITH NO COMORBIDITIES THAT AFFECT OCCUPATIONAL PERFORMANCE. MODIFICATION OF TASKS OR ASSISTANCE (EG, PHYSICAL OR VERBAL) WITH ASSESSMENT(S) IS NOT NECESSARY TO ENABLE COMPLETION OF EVALUATION COMPONENT. TYPICALLY, 30 MINUTES ARE SPENT FACE-TO-FACE WITH THE PATIENT AND/OR FAMILY.",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "97530",
                    "display": "THERAPEUTIC ACTIVITIES",
                }
            ],
            "text": "THERAPEUTIC ACTIVITIES, DIRECT (ONE-ON-ONE) PATIENT CONTACT (USE OF DYNAMIC ACTIVITIES TO IMPROVE FUNCTIONAL PERFORMANCE), EACH 15 MINUTES",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "99213",
                    "display": "OFFICE O/P EST LOW 20-29 MIN",
                }
            ],
            "text": "OFFICE OR OTHER OUTPATIENT VISIT FOR THE EVALUATION AND MANAGEMENT OF AN ESTABLISHED PATIENT, WHICH REQUIRES A MEDICALLY APPROPRIATE HISTORY AND/OR EXAMINATION AND LOW LEVEL OF MEDICAL DECISION MAKING. WHEN USING TIME FOR CODE SELECTION, 20-29 MINUTES OF TOTAL TIME IS SPENT ON THE DATE OF THE ENCOUNTER.",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "99222",
                    "display": "INITIAL HOSPITAL CARE",
                }
            ],
            "text": "INITIAL HOSPITAL CARE, PER DAY, FOR THE EVALUATION AND MANAGEMENT OF A PATIENT, WHICH REQUIRES THESE 3 KEY COMPONENTS: A COMPREHENSIVE HISTORY; A COMPREHENSIVE EXAMINATION; AND MEDICAL DECISION MAKING OF MODERATE COMPLEXITY. COUNSELING AND/OR COORDINATION OF CARE WITH OTHER PHYSICIANS, OTHER QUALIFIED HEALTH CARE PROFESSIONALS, OR AGENCIES ARE PROVIDED CONSISTENT WITH THE NATURE OF THE PROBLEM(S) AND THE PATIENT'S AND/OR FAMILY'S NEEDS. USUALLY, THE PROBLEM(S) REQUIRING ADMISSION ARE OF MODERATE SEVERITY. TYPICALLY, 50 MINUTES ARE SPENT AT THE BEDSIDE AND ON THE PATIENT'S HOSPITAL FLOOR OR UNIT.",
        },
        {
            "coding": [
                {
                    "system": "http://www.ama-assn.org/go/cpt",
                    "code": "99238",
                    "display": "HOSPITAL DISCHARGE DAY",
                }
            ],
            "text": "HOSPITAL DISCHARGE DAY MANAGEMENT; 30 MINUTES OR LESS",
        },
    ],
    "serviceType": {"text": "inpatient"},
    "subject": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/43000199",
        "display": "Ms. Carlita746 Kautzer186",
    },
    "period": {"start": "2021-11-29", "end": "2021-12-01"},
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://www.va.gov/Terminology/VistADefinedTerms/9000010-.07",
                    "version": "9",
                    "code": "780.4",
                    "display": "DIZZINESS AND GIDDINESS",
                }
            ],
            "text": "DIZZINESS AND GIDDINESS",
        }
    ],
    "hospitalization": {
        "dischargeDisposition": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/discharge-disposition",
                    "code": "X",
                    "display": "RETURN TO COMMUNITY-INDEPENDENT",
                }
            ],
            "text": "RETURN TO COMMUNITY-INDEPENDENT",
        }
    },
    "location": [
        {
            "location": {
                "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-2FPCKUIXVR7RJLLG34XVWGZERM000000",
                "display": "MENTAL HEALTH SERVICES",
            }
        }
    ],
    "serviceProvider": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-YCRI7L52BYQL63ZFALGWIWF2WU000000",
        "display": "WASHINGTON VA MEDICAL CENTER",
    },
    "class": {"display": "IMP"},
}

MOCK_IMMUNIZATION = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 6,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Immunization?patient=1000003&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Immunization?patient=1000003&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Immunization?patient=1000003&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Immunization?patient=1000003&_count=1&page=6",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Immunization/I2-5ED3EJGWQMUZVD56BEK252R5UM000000",
            "resource": {
                "resourceType": "Immunization",
                "id": "I2-5ED3EJGWQMUZVD56BEK252R5UM000000",
                "status": "completed",
                "vaccineCode": {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/sid/cvx",
                            "code": "140",
                            "display": "INFLUENZA, SEASONAL, INJECTABLE, PRESERVATIVE FREE",
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/cvx",
                            "code": "88",
                            "display": "VACCINE GROUP: FLU",
                        },
                    ],
                    "text": "Influenza, seasonal, injectable, preservative free",
                },
                "patient": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1000003",
                    "display": "Mr. Tobias236 Wolff180",
                },
                "occurrenceDateTime": "1992-12-12T15:08:09Z",
                "primarySource": True,
                "location": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-2FPCKUIXVR7RJLLG34XVWGZERM000000",
                    "display": "MENTAL HEALTH SERVICES",
                },
                "doseQuantity": {
                    "value": 0.3,
                    "unit": "mL",
                    "system": "http://unitsofmeasure.org",
                    "code": "mL",
                },
                "note": [
                    {
                        "text": "Dose #20 of 101 of Influenza seasonal injectable preservative free vaccine administered."
                    }
                ],
                "reaction": [{"detail": {"display": "Other"}}],
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_IMMUNIZATION_ID = {
    "resourceType": "Immunization",
    "id": "I2-5ED3EJGWQMUZVD56BEK252R5UM000000",
    "status": "completed",
    "vaccineCode": {
        "coding": [
            {
                "system": "http://hl7.org/fhir/sid/cvx",
                "code": "140",
                "display": "INFLUENZA, SEASONAL, INJECTABLE, PRESERVATIVE FREE",
            },
            {
                "system": "http://hl7.org/fhir/sid/cvx",
                "code": "88",
                "display": "VACCINE GROUP: FLU",
            },
        ],
        "text": "Influenza, seasonal, injectable, preservative free",
    },
    "patient": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1000003",
        "display": "Mr. Tobias236 Wolff180",
    },
    "occurrenceDateTime": "1992-12-12T15:08:09Z",
    "primarySource": True,
    "location": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-2FPCKUIXVR7RJLLG34XVWGZERM000000",
        "display": "MENTAL HEALTH SERVICES",
    },
    "doseQuantity": {
        "value": 0.3,
        "unit": "mL",
        "system": "http://unitsofmeasure.org",
        "code": "mL",
    },
    "note": [
        {
            "text": "Dose #20 of 101 of Influenza seasonal injectable preservative free vaccine administered."
        }
    ],
    "reaction": [{"detail": {"display": "Other"}}],
}

MOCK_LOCATION = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location?_id=I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000&page=1&_count=15",
        },
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location?_id=I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000&page=1&_count=15",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location?_id=I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000&page=1&_count=15",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
            "resource": {
                "resourceType": "Location",
                "id": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
                "status": "active",
                "name": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
                "description": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
                "mode": "instance",
                "type": [
                    {
                        "coding": [{"display": "OUTPATIENT CLINIC"}],
                        "text": "OUTPATIENT CLINIC",
                    }
                ],
                "telecom": [{"system": "phone", "value": "908-647-0180 EXT 4437"}],
                "address": {
                    "text": "151 KNOLLCROFT ROAD LYONS NJ 07939",
                    "line": ["151 KNOLLCROFT ROAD"],
                    "city": "LYONS",
                    "state": "NJ",
                    "postalCode": "07939",
                },
                "physicalType": {
                    "coding": [{"display": "BUILDING 7"}],
                    "text": "BUILDING 7",
                },
                "managingOrganization": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-TYIC2AW2NXNADER4SKRKJQZWRE000000",
                    "display": "LYONS VA MEDICAL CENTER",
                },
            },
        }
    ],
}

MOCK_LOCATION_ID = {
    "resourceType": "Location",
    "id": "I2-4KG3N5YUSPTWD3DAFMLMRL5V5U000000",
    "status": "active",
    "name": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
    "description": "VISUAL IMPAIRMENT SVCS OUTPATIENT REHAB (VISOR)",
    "mode": "instance",
    "type": [
        {"coding": [{"display": "OUTPATIENT CLINIC"}], "text": "OUTPATIENT CLINIC"}
    ],
    "telecom": [{"system": "phone", "value": "908-647-0180 EXT 4437"}],
    "address": {
        "text": "151 KNOLLCROFT ROAD LYONS NJ 07939",
        "line": ["151 KNOLLCROFT ROAD"],
        "city": "LYONS",
        "state": "NJ",
        "postalCode": "07939",
    },
    "physicalType": {"coding": [{"display": "BUILDING 7"}], "text": "BUILDING 7"},
    "managingOrganization": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-TYIC2AW2NXNADER4SKRKJQZWRE000000",
        "display": "LYONS VA MEDICAL CENTER",
    },
}

MOCK_MEDICATION = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Medication?identifier=I2-EKB436MCBFA2QLFPGWSBO66SP4000000&page=1&_count=30",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Medication?identifier=I2-EKB436MCBFA2QLFPGWSBO66SP4000000&page=1&_count=30",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Medication?identifier=I2-EKB436MCBFA2QLFPGWSBO66SP4000000&page=1&_count=30",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Medication/I2-EKB436MCBFA2QLFPGWSBO66SP4000000",
            "resource": {
                "resourceType": "Medication",
                "id": "I2-EKB436MCBFA2QLFPGWSBO66SP4000000",
                "text": {
                    "status": "additional",
                    "div": "<div>Levora 0.15/30 28 Day Pack</div>",
                },
                "identifier": [{"id": "4003210"}],
                "code": {
                    "coding": [
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "748879",
                            "display": "Levora 0.15/30 28 Day Pack",
                        }
                    ],
                    "text": "Levora 0.15/30 28 Day Pack",
                },
                "form": {"text": "1 dose(s) 1 time(s) per 1 days"},
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_MEDICATION_ID = {
    "resourceType": "Medication",
    "id": "I2-EKB436MCBFA2QLFPGWSBO66SP4000000",
    "text": {"status": "additional", "div": "<div>Levora 0.15/30 28 Day Pack</div>"},
    "identifier": [{"id": "4003210"}],
    "code": {
        "coding": [
            {
                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                "code": "748879",
                "display": "Levora 0.15/30 28 Day Pack",
            }
        ],
        "text": "Levora 0.15/30 28 Day Pack",
    },
    "form": {"text": "1 dose(s) 1 time(s) per 1 days"},
}

MOCK_MEDICATION_REQUEST = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 18,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/MedicationRequest?patient=1000003&page=1&_count=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/MedicationRequest?patient=1000003&page=1&_count=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/MedicationRequest?patient=1000003&page=2&_count=1",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/MedicationRequest?patient=1000003&page=18&_count=1",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/MedicationRequest/I2-HMBZL7OOOH76YG6DOY65IWJS3Q000000",
            "resource": {
                "resourceType": "MedicationRequest",
                "id": "I2-HMBZL7OOOH76YG6DOY65IWJS3Q000000",
                "status": "active",
                "intent": "plan",
                "reportedBoolean": True,
                "medicationReference": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Medication/I2-EPP7ITEEIPLTRHJNTNLRIGG5MY000000",
                    "display": "Hydrochlorothiazide 6.25 MG",
                },
                "subject": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1000003",
                    "display": "Mr. Tobias236 Wolff180",
                },
                "authoredOn": "1970-11-14T15:08:09Z",
                "_requester": {
                    "extension": [
                        {
                            "url": "https://hl7.org/fhir/extension-data-absent-reason.html",
                            "valueCode": "unknown",
                        }
                    ]
                },
                "note": [{"text": "Hydrochlorothiazide 6.25 MG"}],
                "dosageInstruction": [
                    {
                        "text": "Once per day.",
                        "timing": {
                            "repeat": {
                                "boundsPeriod": {"start": "1970-11-14T15:08:09Z"}
                            },
                            "code": {"text": "As directed by physician."},
                        },
                        "route": {"text": "As directed by physician."},
                    }
                ],
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_MEDICATION_REQUEST_ID = {
    "resourceType": "MedicationRequest",
    "id": "I2-HMBZL7OOOH76YG6DOY65IWJS3Q000000",
    "status": "active",
    "intent": "plan",
    "reportedBoolean": True,
    "medicationReference": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Medication/I2-EPP7ITEEIPLTRHJNTNLRIGG5MY000000",
        "display": "Hydrochlorothiazide 6.25 MG",
    },
    "subject": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1000003",
        "display": "Mr. Tobias236 Wolff180",
    },
    "authoredOn": "1970-11-14T15:08:09Z",
    "_requester": {
        "extension": [
            {
                "url": "https://hl7.org/fhir/extension-data-absent-reason.html",
                "valueCode": "unknown",
            }
        ]
    },
    "note": [{"text": "Hydrochlorothiazide 6.25 MG"}],
    "dosageInstruction": [
        {
            "text": "Once per day.",
            "timing": {
                "repeat": {"boundsPeriod": {"start": "1970-11-14T15:08:09Z"}},
                "code": {"text": "As directed by physician."},
            },
            "route": {"text": "As directed by physician."},
        }
    ],
}

MOCK_OBSERVATION = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 263,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation?patient=1000005&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation?patient=1000005&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation?patient=1000005&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation?patient=1000005&_count=1&page=263",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Observation/I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000",
            "resource": {
                "resourceType": "Observation",
                "id": "I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000",
                "meta": {"lastUpdated": "1998-04-15T05:56:37Z"},
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                "code": "laboratory",
                                "display": "Laboratory",
                            }
                        ],
                        "text": "Laboratory",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://loinc.org",
                            "code": "2339-0",
                            "display": "Glucose",
                        }
                    ],
                    "text": "Glucose",
                },
                "subject": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1000005",
                    "display": "Mr. Shane235 Bartell116",
                },
                "effectiveDateTime": "1998-03-16T05:56:37Z",
                "issued": "1998-03-16T05:56:37Z",
                "performer": [
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-4ZXYC2SQAZCHMOWPPFNLOY65GE000000",
                        "display": "DR. THOMAS359 REYNOLDS206 PHD",
                    }
                ],
                "valueQuantity": {
                    "value": 78.278855002875,
                    "unit": "mg/dL",
                    "system": "http://unitsofmeasure.org",
                    "code": "mg/dL",
                },
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_OBSERVATION_ID = {
    "resourceType": "Observation",
    "id": "I2-ILWORI4YUOUAR5H2GCH6ATEFRM000000",
    "meta": {"lastUpdated": "1998-04-15T05:56:37Z"},
    "status": "final",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "laboratory",
                    "display": "Laboratory",
                }
            ],
            "text": "Laboratory",
        }
    ],
    "code": {
        "coding": [
            {"system": "http://loinc.org", "code": "2339-0", "display": "Glucose"}
        ],
        "text": "Glucose",
    },
    "subject": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/1000005",
        "display": "Mr. Shane235 Bartell116",
    },
    "effectiveDateTime": "1998-03-16T05:56:37Z",
    "issued": "1998-03-16T05:56:37Z",
    "performer": [
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-4ZXYC2SQAZCHMOWPPFNLOY65GE000000",
            "display": "DR. THOMAS359 REYNOLDS206 PHD",
        }
    ],
    "valueQuantity": {
        "value": 78.278855002875,
        "unit": "mg/dL",
        "system": "http://unitsofmeasure.org",
        "code": "mg/dL",
    },
}

MOCK_ORGANIZATION = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization?address-state=NJ&_count=30&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization?address-state=NJ&_count=30&page=1",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization?address-state=NJ&_count=30&page=1",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-TYIC2AW2NXNADER4SKRKJQZWRE000000",
            "resource": {
                "resourceType": "Organization",
                "id": "I2-TYIC2AW2NXNADER4SKRKJQZWRE000000",
                "identifier": [
                    {"system": "http://hl7.org/fhir/sid/us-npi", "value": "1396794293"}
                ],
                "active": True,
                "name": "LYONS- VA NEW JERSEY HCS",
                "address": [
                    {
                        "text": "151 KNOLLCROFT ROAD LYONS NJ 07939-5001",
                        "line": ["151 KNOLLCROFT ROAD"],
                        "city": "LYONS",
                        "state": "NJ",
                        "postalCode": "07939-5001",
                    }
                ],
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_ORGANIZATION_ID = {
    "resourceType": "Organization",
    "id": "I2-TYIC2AW2NXNADER4SKRKJQZWRE000000",
    "identifier": [{"system": "http://hl7.org/fhir/sid/us-npi", "value": "1396794293"}],
    "active": True,
    "name": "LYONS- VA NEW JERSEY HCS",
    "address": [
        {
            "text": "151 KNOLLCROFT ROAD LYONS NJ 07939-5001",
            "line": ["151 KNOLLCROFT ROAD"],
            "city": "LYONS",
            "state": "NJ",
            "postalCode": "07939-5001",
        }
    ],
}

MOCK_PATIENT = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient?identifier=1017283148V813263&page=1&_count=15",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient?identifier=1017283148V813263&page=1&_count=15",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient?identifer=1017283148V813263&page=1&_count=15",
        },
    ],
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "id": "2000163",
                "extension": [
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "system": "https://www.hl7.org/fhir/us/core/CodeSystem-cdcrec.html",
                                    "code": "2016-3",
                                    "display": "White",
                                },
                            },
                            {"url": "text", "valueString": "White"},
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                    },
                    {
                        "extension": [
                            {
                                "url": "ombCategory",
                                "valueCoding": {
                                    "system": "https://www.hl7.org/fhir/us/core/CodeSystem-cdcrec.html",
                                    "code": "2186-5",
                                    "display": "Not Hispanic or Latino",
                                },
                            },
                            {"url": "text", "valueString": "Not Hispanic or Latino"},
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                    },
                    {
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                        "valueCode": "M",
                    },
                ],
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {"system": "http://hl7.org/fhir/v2/0203", "code": "MR"}
                            ]
                        },
                        "system": "http://va.gov/mpi",
                        "value": "2000163",
                    },
                    {
                        "use": "official",
                        "type": {
                            "coding": [
                                {"system": "http://hl7.org/fhir/v2/0203", "code": "SB"}
                            ]
                        },
                        "system": "http://hl7.org/fhir/sid/us-ssn",
                        "value": "999-61-4803",
                    },
                ],
                "name": [
                    {
                        "use": "usual",
                        "text": "Mr. Aurelio227 Cruickshank494",
                        "family": "Cruickshank494",
                        "given": ["Aurelio227"],
                    }
                ],
                "telecom": [
                    {"system": "phone", "value": "5555191065", "use": "mobile"},
                    {
                        "system": "email",
                        "value": "Aurelio227.Cruickshank494@email.example",
                    },
                ],
                "gender": "male",
                "birthDate": "1995-02-06",
                "deceasedBoolean": False,
                "address": [
                    {
                        "line": ["909 Rohan Highlands"],
                        "city": "Mesa",
                        "state": "Arizona",
                        "postalCode": "85120",
                    }
                ],
                "maritalStatus": {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/R4/v3/NullFlavor/cs.html",
                            "code": "UNK",
                            "display": "unknown",
                        }
                    ],
                    "text": "unknown",
                },
            }
        }
    ],
}

MOCK_PATIENT_ID = {
    "resourceType": "Patient",
    "id": "2000163",
    "extension": [
        {
            "extension": [
                {
                    "url": "ombCategory",
                    "valueCoding": {
                        "system": "https://www.hl7.org/fhir/us/core/CodeSystem-cdcrec.html",
                        "code": "2016-3",
                        "display": "White",
                    },
                },
                {"url": "text", "valueString": "White"},
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
        },
        {
            "extension": [
                {
                    "url": "ombCategory",
                    "valueCoding": {
                        "system": "https://www.hl7.org/fhir/us/core/CodeSystem-cdcrec.html",
                        "code": "2186-5",
                        "display": "Not Hispanic or Latino",
                    },
                },
                {"url": "text", "valueString": "Not Hispanic or Latino"},
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
        },
        {
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
            "valueCode": "M",
        },
    ],
    "identifier": [
        {
            "use": "usual",
            "type": {
                "coding": [{"system": "http://hl7.org/fhir/v2/0203", "code": "MR"}]
            },
            "system": "http://va.gov/mpi",
            "value": "2000163",
        },
        {
            "use": "official",
            "type": {
                "coding": [{"system": "http://hl7.org/fhir/v2/0203", "code": "SB"}]
            },
            "system": "http://hl7.org/fhir/sid/us-ssn",
            "value": "999-61-4803",
        },
    ],
    "name": [
        {
            "use": "usual",
            "text": "Mr. Aurelio227 Cruickshank494",
            "family": "Cruickshank494",
            "given": ["Aurelio227"],
        }
    ],
    "telecom": [
        {"system": "phone", "value": "5555191065", "use": "mobile"},
        {"system": "email", "value": "Aurelio227.Cruickshank494@email.example"},
    ],
    "gender": "male",
    "birthDate": "1995-02-06",
    "deceasedBoolean": False,
    "address": [
        {
            "line": ["909 Rohan Highlands"],
            "city": "Mesa",
            "state": "Arizona",
            "postalCode": "85120",
        }
    ],
    "maritalStatus": {
        "coding": [
            {
                "system": "http://hl7.org/fhir/R4/v3/NullFlavor/cs.html",
                "code": "UNK",
                "display": "unknown",
            }
        ],
        "text": "unknown",
    },
}

MOCK_PRACTITIONER = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner?_id=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner?_id=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner?_id=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
            "resource": {
                "resourceType": "Practitioner",
                "id": "I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {"system": "http://hl7.org/fhir/v2/0203", "code": "MR"}
                            ]
                        },
                        "system": "http://va.gov/mpi",
                        "value": "1015517260V990420",
                        "assigner": {"display": "Master Patient Index"},
                    },
                    {"system": "http://hl7.org/fhir/sid/us-npi", "value": "1932127842"},
                ],
                "active": True,
                "name": [
                    {
                        "family": "DOE922",
                        "given": ["JANE460"],
                        "prefix": ["DR."],
                        "suffix": ["MD"],
                    }
                ],
                "telecom": [
                    {"system": "phone", "value": "555-555-1137", "use": "work"},
                    {"system": "phone", "value": "555-4055", "use": "home"},
                    {"system": "pager", "value": "5-541", "use": "mobile"},
                ],
                "address": [
                    {
                        "line": ["555 E 5TH ST", "SUITE B"],
                        "city": "CHEYENNE",
                        "state": "WYOMING",
                        "postalCode": "82001",
                        "period": {"start": "2010-01-01", "end": "2015-04-02"},
                    }
                ],
                "gender": "female",
                "birthDate": "1964-02-23",
                "qualification": [{"code": {"text": "MD"}}],
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_PRACTITIONER_ID = {
    "resourceType": "Practitioner",
    "id": "I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
    "identifier": [
        {
            "use": "usual",
            "type": {
                "coding": [{"system": "http://hl7.org/fhir/v2/0203", "code": "MR"}]
            },
            "system": "http://va.gov/mpi",
            "value": "1015517260V990420",
            "assigner": {"display": "Master Patient Index"},
        },
        {"system": "http://hl7.org/fhir/sid/us-npi", "value": "1932127842"},
    ],
    "active": True,
    "name": [
        {"family": "DOE922", "given": ["JANE460"], "prefix": ["DR."], "suffix": ["MD"]}
    ],
    "telecom": [
        {"system": "phone", "value": "555-555-1137", "use": "work"},
        {"system": "phone", "value": "555-4055", "use": "home"},
        {"system": "pager", "value": "5-541", "use": "mobile"},
    ],
    "address": [
        {
            "line": ["555 E 5TH ST", "SUITE B"],
            "city": "CHEYENNE",
            "state": "WYOMING",
            "postalCode": "82001",
            "period": {"start": "2010-01-01", "end": "2015-04-02"},
        }
    ],
    "gender": "female",
    "birthDate": "1964-02-23",
    "qualification": [{"code": {"text": "MD"}}],
}

MOCK_PRACTITIONER_ROLE = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/PractitionerRole?practitioner.identifier=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/PractitionerRole?practitioner.identifier=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/PractitionerRole?practitioner.identifier=I2-HRJI2MVST2IQSPR7U5SACWIWZA000000&_count=30&page=1",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/PractitionerRole/I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000",
            "resource": {
                "resourceType": "PractitionerRole",
                "id": "I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000",
                "active": True,
                "practitioner": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
                    "display": "DOE922,JANE460",
                },
                "organization": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000",
                    "display": "CHEYENNE VA MEDICAL",
                },
                "code": [
                    {
                        "coding": [
                            {
                                "system": "http://hl7.org/fhir/practitioner-role",
                                "code": "PHYSICIAN",
                                "display": "PSYCHOLOGIST",
                            }
                        ],
                        "text": "PSYCHOLOGIST",
                    }
                ],
                "specialty": [
                    {
                        "coding": [
                            {
                                "system": "http://nucc.org/provider-taxonomy",
                                "code": "V111500",
                            }
                        ]
                    },
                    {
                        "coding": [
                            {
                                "system": "http://nucc.org/provider-taxonomy",
                                "code": "V111000",
                            }
                        ]
                    },
                    {
                        "coding": [
                            {
                                "system": "http://nucc.org/provider-taxonomy",
                                "code": "V110900",
                            }
                        ]
                    },
                    {
                        "coding": [
                            {
                                "system": "http://nucc.org/provider-taxonomy",
                                "code": "207Q00000X",
                            }
                        ]
                    },
                ],
                "location": [
                    {
                        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-3JYDMXC6RXTU4H25KRVXATSEJQ000000",
                        "display": "ZZCHY LASTNAME MEDICAL",
                    }
                ],
                "healthcareService": [{"display": "MEDICAL SERVICE"}],
                "telecom": [
                    {"system": "phone", "value": "555-555-1137"},
                    {"system": "phone", "value": "555-4055"},
                    {"system": "pager", "value": "5-541"},
                ],
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_PRACTITIONER_ROLE_ID = {
    "resourceType": "PractitionerRole",
    "id": "I2-6KYHN4VYERE5OHKPXWAPAU5BO4000000",
    "active": True,
    "practitioner": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Practitioner/I2-HRJI2MVST2IQSPR7U5SACWIWZA000000",
        "display": "DOE922,JANE460",
    },
    "organization": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Organization/I2-AKOTGEFSVKFJOPUKHIVJAH5VQU000000",
        "display": "CHEYENNE VA MEDICAL",
    },
    "code": [
        {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/practitioner-role",
                    "code": "PHYSICIAN",
                    "display": "PSYCHOLOGIST",
                }
            ],
            "text": "PSYCHOLOGIST",
        }
    ],
    "specialty": [
        {
            "coding": [
                {"system": "http://nucc.org/provider-taxonomy", "code": "V111500"}
            ]
        },
        {
            "coding": [
                {"system": "http://nucc.org/provider-taxonomy", "code": "V111000"}
            ]
        },
        {
            "coding": [
                {"system": "http://nucc.org/provider-taxonomy", "code": "V110900"}
            ]
        },
        {
            "coding": [
                {"system": "http://nucc.org/provider-taxonomy", "code": "207Q00000X"}
            ]
        },
    ],
    "location": [
        {
            "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-3JYDMXC6RXTU4H25KRVXATSEJQ000000",
            "display": "ZZCHY LASTNAME MEDICAL",
        }
    ],
    "healthcareService": [{"display": "MEDICAL SERVICE"}],
    "telecom": [
        {"system": "phone", "value": "555-555-1137"},
        {"system": "phone", "value": "555-4055"},
        {"system": "pager", "value": "5-541"},
    ],
}

MOCK_PROCEDURE = {
    "resourceType": "Bundle",
    "type": "searchset",
    "total": 10,
    "link": [
        {
            "relation": "first",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Procedure?patient=38000008&_count=1&page=1",
        },
        {
            "relation": "self",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Procedure?patient=38000008&_count=1&page=1",
        },
        {
            "relation": "next",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Procedure?patient=38000008&_count=1&page=2",
        },
        {
            "relation": "last",
            "url": "https://sandbox-api.va.gov/services/fhir/v0/r4/Procedure?patient=38000008&_count=1&page=10",
        },
    ],
    "entry": [
        {
            "fullUrl": "https://sandbox-api.va.gov/services/fhir/v0/r4/Procedure/I2-TD6AZ3E7TO2DYFFXQOIWZNC3FM000000",
            "resource": {
                "resourceType": "Procedure",
                "id": "I2-TD6AZ3E7TO2DYFFXQOIWZNC3FM000000",
                "meta": {"lastUpdated": "1986-08-08T11:27:35Z"},
                "status": "completed",
                "code": {
                    "coding": [
                        {
                            "system": "http://www.ama-assn.org/go/cpt",
                            "code": "XXXXX",
                            "display": "Documentation of current medications",
                        }
                    ],
                    "text": "Documentation of current medications",
                },
                "subject": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/38000008",
                    "display": "Ethan766 Auer97",
                },
                "performedDateTime": "1986-07-09T11:27:35Z",
                "location": {
                    "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-2FPCKUIXVR7RJLLG34XVWGZERM000000",
                    "display": "MENTAL HEALTH SERVICES",
                },
            },
            "search": {"mode": "match"},
        }
    ],
}

MOCK_PROCEDURE_ID = {
    "resourceType": "Procedure",
    "id": "I2-TD6AZ3E7TO2DYFFXQOIWZNC3FM000000",
    "meta": {"lastUpdated": "1986-08-08T11:27:35Z"},
    "status": "completed",
    "code": {
        "coding": [
            {
                "system": "http://www.ama-assn.org/go/cpt",
                "code": "XXXXX",
                "display": "Documentation of current medications",
            }
        ],
        "text": "Documentation of current medications",
    },
    "subject": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Patient/38000008",
        "display": "Ethan766 Auer97",
    },
    "performedDateTime": "1986-07-09T11:27:35Z",
    "location": {
        "reference": "https://sandbox-api.va.gov/services/fhir/v0/r4/Location/I2-2FPCKUIXVR7RJLLG34XVWGZERM000000",
        "display": "MENTAL HEALTH SERVICES",
    },
}

MOCK_METADATA = {
    "resourceType": "CapabilityStatement",
    "id": "example-api-capability",
    "version": "1.23.456",
    "name": "API Management Platform | Example - US Core",
    "title": "API Management Platform | Example - US Core",
    "status": "active",
    "experimental": False,
    "date": "2021-11-10T17:00:00Z",
    "publisher": "Department of Veterans Affairs",
    "contact": [
        {
            "name": "Example Contact",
            "telecom": [{"system": "email", "value": "example.email@foo.com"}],
        }
    ],
    "description": "Read and search support for FHIR resources.",
    "kind": "capability",
    "software": {
        "name": "gov.va.api.examples:example-app",
        "version": "1.23.456",
        "releaseDate": "2021-11-01T17:00:00Z",
    },
    "implementation": {
        "description": "API Management Platform | Example - US Core",
        "url": "https://sandbox-api.va.gov/services/fhir/r4",
    },
    "fhirVersion": "4.0.1",
    "format": ["application/json", "application/fhir+json"],
    "rest": [
        {
            "mode": "server",
            "security": {
                "extension": [
                    {
                        "extension": [
                            {
                                "url": "token",
                                "valueUri": "https://sandbox-api.va.gov/example/token",
                            },
                            {
                                "url": "authorize",
                                "valueUri": "https://sandbox-api.va.gov/example/authorize",
                            },
                            {
                                "url": "manage",
                                "valueUri": "https://sandbox-api.va.gov/example/manage",
                            },
                            {
                                "url": "revoke",
                                "valueUri": "https://sandbox-api.va.gov/example/revoke",
                            },
                        ],
                        "url": "http://fhir-registry.smarthealthit.org/StructureDefinition/oauth-uris",
                    }
                ],
                "cors": True,
                "service": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/restful-security-service",
                                "code": "SMART-on-FHIR",
                                "display": "SMART-on-FHIR",
                            }
                        ],
                        "text": "SMART-on-FHIR",
                    }
                ],
                "description": "http://docs.smarthealthit.org/",
            },
            "resource": [
                {
                    "type": "Example Resource",
                    "profile": "http://example-resource-profile.com",
                    "interaction": [
                        {
                            "code": "search-type",
                            "documentation": "Example search interaction.",
                        },
                        {"code": "read", "documentation": "Example read interaction."},
                    ],
                    "versioning": "no-version",
                    "referencePolicy": ["literal"],
                    "searchParam": [{"name": "example_param", "type": "token"}],
                }
            ],
        }
    ],
}

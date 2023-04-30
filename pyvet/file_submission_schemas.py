import base64
from datetime import datetime
from dataclasses import dataclass

from typing import Annotated

BytesBase64 = Annotated[bytes, bytes]


@dataclass
class Address:
    numberAndStreet: str
    city: str
    country: str
    zipFirstFive: str
    aptUnitNumber: int | None = None
    state: str | None = None
    zipLastFour: str | None = None
    additionalProperties: bool | None = None


@dataclass
class Phone:
    areaCode: str
    phoneNumber: str
    countryCode: str | None = None
    phoneNumberExtstring: str | None = None


@dataclass
class Veteran:
    address: Address
    phone: Phone
    emailAddress: str
    serviceBranch: str | None = None
    serviceBranchOtherstring: str | None = None


@dataclass
class Claimant:
    firstName: str
    lastName: str
    address: Address
    phone: Phone
    email: str
    relationship: str
    middleInitial: str | None = None


@dataclass
class ServiceOrganization:
    poaCode: str
    description: str | None = None
    organizationNamestring: str | None = None
    firstName: str | None = None
    lastName: str | None = None
    jobTitle: str | None = None
    address: Address | None = None
    email: str | None = None


@dataclass
class Signature:
    # Base64 encoded png image of the signature.
    title: BytesBase64


@dataclass
class Signatures:
    veteran: Signature
    representative: Signature


@dataclass
class POAForm:
    veteran: Veteran
    claimant: Claimant
    serviceOrganization: ServiceOrganization
    recordConsent: bool
    signatures: Signatures
    consentLimits: str | None = None
    consentAddressChangeboolean: bool | None = None

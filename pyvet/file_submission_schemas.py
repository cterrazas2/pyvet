"""Dataclasses for Intent to File API"""
# pylint: skip-file
import base64
from datetime import datetime
from dataclasses import dataclass

from typing import Annotated

BytesBase64 = Annotated[bytes, bytes]


@dataclass
class Address:
    """Address dataclass for Intent to File API"""

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
    """Phone dataclass for Intent to File API"""

    areaCode: str
    phoneNumber: str
    countryCode: str | None = None
    phoneNumberExtstring: str | None = None


@dataclass
class Veteran:
    """Veteran dataclass for Intent to File API"""

    address: Address
    phone: Phone
    emailAddress: str
    serviceBranch: str | None = None
    serviceBranchOtherstring: str | None = None


@dataclass
class Claimant:
    """Claimant dataclass for Intent to File API"""

    firstName: str
    lastName: str
    address: Address
    phone: Phone
    email: str
    relationship: str
    middleInitial: str | None = None


@dataclass
class ServiceOrganization:
    """Service Organization dataclass for Intent to File API"""

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
    """Signature dataclass for Intent to File API"""

    # Base64 encoded png image of the signature.
    title: BytesBase64


@dataclass
class Signatures:
    """Signatures dataclass for Intent to File API"""

    veteran: Signature
    representative: Signature


@dataclass
class POAForm:
    """POA Form dataclass for Intent to File API"""

    veteran: Veteran
    claimant: Claimant
    serviceOrganization: ServiceOrganization
    recordConsent: bool
    signatures: Signatures
    consentLimits: str | None = None
    consentAddressChangeboolean: bool | None = None

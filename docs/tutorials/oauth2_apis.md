# VA Oauth2 APIs example requests

## Veteran Verification

```python
from pyvet.veteran.verification.api import get_status

# Confirm veteran status, will return confirmed or not confirmed. Note, oidc handshake is happening here.
status = get_status() # {'veteran_status': confirmed}
```

## Veteran Benefits Intake

You can get all claims or a specific claim for a veteran with `pyvet`.

```python
from pyvet.benefits.claims.api import get_claim, get_claims

va_claims = get_claims(
    ssn="796130115",
    first_name="Tamara",
    last_name="Ellis",
    birth_date="1967-06-19",
)

va_claim = get_claim(
    claim_id="600106271",
    ssn="796130115",
    first_name="Tamara",
    last_name="Ellis",
    birth_date="1967-06-19",
)

```

# Authorization

## Oauth2 APIs

`pyvet` communicates to all VA Oauth Apis via an Authorization Code Flow. When trying to communicate with an oauth2 API,
`pyvet` will utilize [`oidc`](https://openid.net/connect/) to ensure the veteran is approved by a VA-approved Identity Provider (IDP) like [ID.me](https://www.id.me) or [Login.gov](https://login.gov). `pyvet` performs the entire authentication by directing the consumer (the veteran) to two main steps.

1. The login process will begin the authentication process by receiving authorization via a Proof Key for Code Exchange (PCKE). This results in a `code` from the VA's `/authorization` endpoint.
2. The authentication continues to the `/token` endpoint, utilizing the `code` received from step 1. Upon success, a bearer `token` (along with other metadata) is provided. `pyvet` will then return the desired data ftom the VA oauth2 API to the consumer.

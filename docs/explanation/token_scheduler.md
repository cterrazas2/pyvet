# Token Scheduler

## Least Privilege

`pyvet` uses the principle of
[least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)
when interacting with various VA apis. A veteran must initially request and
authorize access for each api and then `pyvet` will place the bearer token in a
cache.

Below is an example of the token cache for a va api
name and its token, or key value pair respectively.

```python3
{
    'veteran': 'somerandomtoken',
    'claims': 'somerandomtoken',
    ...
}
```

### Eviction Policy

The token cache will be updated on initial entry of a bearer token and then
once it becomes invalid (expired or revoked). The refresh token will be used
to retrieve another token. If the refresh token is expired, then the entire
authentication process is initiated for the veteran's approval.

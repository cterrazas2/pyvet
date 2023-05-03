# Token Cache

## Least Privilege

`pyvet` uses the principle of least privilege when interacting with various VA
apis. A veteran must initially request and authorize access for each api and
then `pyvet` will place the bearer token in a cache.

The token cache will be updated on initial entry and then once the bearer
token expires, utilizing the refresh token to retrieve another token. Below is
an example of the token cache for a va api name and its token, or key value
pair respectively.

```python3
{
    'veteran': 'somerandomtoken',
    'claims': 'somerandomtoken',
    ...
}
```

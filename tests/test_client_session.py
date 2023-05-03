import unittest

from pyvet import creds


class TestClientSession(unittest.TestCase):
    def setUp(self):
        self.headers = creds.API_KEY_HEADER

    def test_get_session_headers(self):
        from pyvet.client import current_session

        assert current_session.headers == self.headers


if __name__ == "__main__":
    unittest.main()

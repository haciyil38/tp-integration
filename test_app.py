import unittest
from app import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("ClientHub", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()

""" Test views luz"""

from django.test import TestCase, Client
from ..models import Room


class ModelTests(TestCase):
    """Test class for models of the project"""

    def setUp(self):
        """Set up"""
        Room.objects.create(name="SALA", size=60)
        self.client = Client()

    def test_basura(self):
        """Test inicial"""
        response = self.client.get("/project/room/all/")

        self.assertEqual(response.status_code, 200)

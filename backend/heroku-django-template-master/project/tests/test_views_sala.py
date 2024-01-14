""" Test for views_sala.py """

from django.test import TestCase, Client
from ..models import Room


class SalaTests(TestCase):
    """Test class for salas"""

    def setUp(self):
        """Set up"""
        self.client = Client()

    def test_index(self):
        """Test for index"""

        response = self.client.get("/project/")

        self.assertEqual(response.status_code, 200)

    def test_home(self):
        """Test for home"""

        response = self.client.get("/project/home/")

        self.assertEqual(response.status_code, 200)

    def test_room_all(self):
        """Test for room all"""

        response = self.client.get("/project/room/all/")

        self.assertEqual(response.status_code, 404)

        Room.objects.create(name="SALA", size=60)

        response = self.client.get("/project/room/all/")

        self.assertEqual(response.status_code, 200)

        Room.objects.filter(name="SALA").delete()

        response = self.client.get("/project/room/all/")

        self.assertEqual(response.status_code, 404)

    def test_room_create(self):
        """Test for room create"""

        response = self.client.post(
            "/project/room/create/", {"name": "SALA", "size": 60}
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/project/room/create/", {"name": "SALA", "size": 60}
        )

        self.assertEqual(response.status_code, 400)

        response = self.client.post(
            "/project/room/create/", {"nam": "SALA", "size": 60}
        )

        self.assertEqual(response.status_code, 400)

        response = self.client.post(
            "/project/room/create/", {"name": "SALA", "siz": 60}
        )

        self.assertEqual(response.status_code, 400)

    def test_room_get(self):
        """Test for room get"""

        response = self.client.get("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)

        Room.objects.create(name="SALA", size=60)

        response = self.client.get("/project/room/SALA/")

        self.assertEqual(response.status_code, 200)

        response = self.client.get("/project/room/SALA1/")

        self.assertEqual(response.status_code, 404)

    def test_room_delete(self):
        """Test for room delete"""

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)

        Room.objects.create(name="SALA", size=60)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)

    def test_room_patch(self):
        """Test for room patch"""

        response = self.client.patch(
            "/project/room/SALA/",
            {"name": "SALA1", "size": 80},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 404)

        Room.objects.create(name="SALA", size=60)

        response = self.client.patch(
            "/project/room/SALA/",
            {"name": "SALA1", "size": 80},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

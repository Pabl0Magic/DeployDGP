""" Test for views_luz.py """

from django.test import TestCase, Client
from ..models import Room, Light


class LuzTests(TestCase):
    """Test class for ventana"""

    def setUp(self):
        """Set up"""
        self.client = Client()
        Room.objects.create(name="SALA", size=60)

    def test_light_all(self):
        """Test for light all"""

        response = self.client.get("/project/room/SALA/light/all/")

        self.assertEqual(response.status_code, 404)

        Light.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/light/all/")

        self.assertEqual(response.status_code, 200)

    def test_light_create(self):
        """Test for light create"""

        response = self.client.post(
            "/project/room/SALA/light/create/", {"id": 1, "room": "SALA"}
        )

        self.assertEqual(response.status_code, 201)

    def test_light_get(self):
        """Test for light get"""

        response = self.client.get("/project/room/SALA/light/1/")

        self.assertEqual(response.status_code, 404)

        Light.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/light/1/")

        self.assertEqual(response.status_code, 200)

    def test_light_delete(self):
        """Test for light delete"""

        Light.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.delete("/project/room/SALA/light/1/")

        self.assertEqual(response.status_code, 204)

    def test_light_patch(self):
        """Test for light patch"""

        Light.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.patch(
            "/project/room/SALA/light/1/", {"id": "2"}, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

    def test_light_add_ts(self):
        """Test for light timestamp add"""

        Light.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.post("/project/room/SALA/light/1/addTs/")

        self.assertEqual(response.status_code, 201)

    def test_light_activity(self):
        """Test for light activity"""

        Light.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/light/1/activity/")

        self.assertEqual(response.status_code, 200)

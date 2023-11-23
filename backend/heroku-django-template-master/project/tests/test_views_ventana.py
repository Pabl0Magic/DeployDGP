""" Test for views_ventana.py """

from django.test import TestCase, Client
from ..models import Room, Window


class VentanaTests(TestCase):
    """Test class for ventana"""

    def setUp(self):
        """Set up"""
        self.client = Client()
        Room.objects.create(name="SALA", size=60)

    def test_window_all(self):
        """Test for window all"""

        response = self.client.get("/project/room/SALA/window/all/")

        self.assertEqual(response.status_code, 404)

        Window.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/window/all/")

        self.assertEqual(response.status_code, 200)

    def test_window_create(self):
        """Test for window create"""

        response = self.client.post(
            "/project/room/SALA/window/create/", {"id": 1, "room": "SALA"}
        )

        self.assertEqual(response.status_code, 201)

    def test_window_get(self):
        """Test for window get"""

        response = self.client.get("/project/room/SALA/window/1/")

        self.assertEqual(response.status_code, 404)

        Window.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/window/1/")

        self.assertEqual(response.status_code, 200)

    def test_window_delete(self):
        """Test for window delete"""

        Window.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.delete("/project/room/SALA/window/1/")

        self.assertEqual(response.status_code, 204)

    def test_window_patch(self):
        """Test for window patch"""
        # REVISAR

    def test_window_add_ts(self):
        """Test for window timestamp add"""

        Window.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.post("/project/room/SALA/window/1/addTs/")

        self.assertEqual(response.status_code, 201)

    def test_window_activity(self):
        """Test for window activity"""

        Window.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/window/1/activity/")

        self.assertEqual(response.status_code, 200)

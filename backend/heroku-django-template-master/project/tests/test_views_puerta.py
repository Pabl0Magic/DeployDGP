""" Test for views_puerta.py """

from django.test import TestCase, Client
from ..models import Room, Door


class PuertaTests(TestCase):
    """Test class for ventana"""

    def setUp(self):
        """Set up"""
        self.client = Client()
        Room.objects.create(name="SALA", size=60)

    def test_door_all(self):
        """Test for door all"""

        response = self.client.get("/project/room/SALA/door/all/")

        self.assertEqual(response.status_code, 404)

        door_instance = Door.objects.create(id=1)
        door_instance.rooms.add(Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/door/all/")

        self.assertEqual(response.status_code, 200)

    def test_door_create(self):
        """Test for door create"""

        response = self.client.post(
            "/project/room/SALA/door/create/", {"id": 1, "rooms": "SALA"}
        )

        self.assertEqual(response.status_code, 201)

    def test_door_get(self):
        """Test for door get"""

        response = self.client.get("/project/room/SALA/door/1/")

        self.assertEqual(response.status_code, 404)

        Door.objects.create(id=1)

        response = self.client.get("/project/room/SALA/door/1/")

        self.assertEqual(response.status_code, 200)

    def test_door_delete(self):
        """Test for door delete"""

        Door.objects.create(id=1)

        response = self.client.delete("/project/room/SALA/door/1/")

        self.assertEqual(response.status_code, 204)

    def test_door_patch(self):
        """Test for door patch"""

        Door.objects.create(id=1)

        response = self.client.patch(
            "/project/room/SALA/door/1/", {"id": "2"}, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

    def test_door_add_ts(self):
        """Test for door timestamp add"""

        Door.objects.create(id=1)

        response = self.client.post("/project/room/SALA/door/1/addTs/")

        self.assertEqual(response.status_code, 201)

    def test_door_activity(self):
        """Test for door activity"""

        Door.objects.create(id=1)

        response = self.client.get("/project/room/SALA/door/1/activity/")

        self.assertEqual(response.status_code, 200)

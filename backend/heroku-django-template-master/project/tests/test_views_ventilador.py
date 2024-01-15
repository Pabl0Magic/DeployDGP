""" Test for views_ventilator.py """

from django.test import TestCase, Client
from ..models import Room, Ventilator


class VentiladorTests(TestCase):
    """Test class for ventiladores"""

    def setUp(self):
        """Set up"""
        self.client = Client()
        Room.objects.create(name="SALA", size=60)

    def test_ventilator_all(self):
        """Test for ventilator all"""

        response = self.client.get("/project/room/SALA/ventilator/all/")

        self.assertEqual(response.status_code, 404)

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/ventilator/all/")

        self.assertEqual(response.status_code, 200)

        Ventilator.objects.filter(id=1).delete()

        response = self.client.get("/project/room/SALA/ventilator/all/")

        self.assertEqual(response.status_code, 404)

    def test_ventilator_create(self):
        """Test for ventilator create"""

        response = self.client.post(
            "/project/room/SALA/ventilator/create/", {"id": 1, "room": "SALA"}
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/project/room/SALA/ventilator/create/", {"roo": "SALA"}
        )

        self.assertEqual(response.status_code, 400)

        response = self.client.post(
            "/project/room/SALA/ventilator/create/", {"room": "SALA2"}
        )

        self.assertEqual(response.status_code, 400)

    def test_ventilator_get(self):
        """Test for ventilator get"""

        response = self.client.get("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 404)

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 200)

        Ventilator.objects.filter(id=1).delete()

        response = self.client.get("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 404)

    def test_ventilator_delete(self):
        """Test for ventilator delete"""

        response = self.client.delete("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 404)

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.delete("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 404)

    def test_ventilator_patch(self):
        """Test for ventilator patch"""

        response = self.client.patch(
            "/project/room/SALA/ventilator/1/",
            {"id": "2"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 404)

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.patch(
            "/project/room/SALA/ventilator/1/",
            {"id": "2"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

    def test_ventilator_add_ts(self):
        """Test for ventilator timestamp add"""
        
        response = self.client.post("/project/room/SALA/ventilator/1/addTs/")

        self.assertEqual(response.status_code, 404)

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.post("/project/room/SALA/ventilator/1/addTs/")

        self.assertEqual(response.status_code, 201)

        Ventilator.objects.filter(id=1).delete()

        response = self.client.post("/project/room/SALA/ventilator/1/addTs/")

        self.assertEqual(response.status_code, 404)

    def test_ventilator_activity(self):
        """Test for ventilator activity"""

        response = self.client.get("/project/room/SALA/ventilator/1/activity/")

        self.assertEqual(response.status_code, 500)

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/ventilator/1/activity/")

        self.assertEqual(response.status_code, 200)

        Ventilator.objects.filter(id=1).delete()

        response = self.client.get("/project/room/SALA/ventilator/1/activity/")

        self.assertEqual(response.status_code, 500)



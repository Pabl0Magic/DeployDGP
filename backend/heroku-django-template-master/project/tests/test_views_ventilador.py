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

        response = self.client.get("/project/room/all/")

        response = self.client.get("/project/room/SALA/ventilator/all/")

    def test_ventilator_create(self):
        """Test for ventilator create"""

        # response = self.client.post(
        #    "/project/room/SALA/ventilator/create/",
        #    {"id": 1, "room": Room.objects.get(name="SALA")}
        # )

        # print(response)

        # self.assertEqual(response.status_code, 201)"""

    def test_ventilator_get(self):
        """Test for ventilator get"""

        response = self.client.get("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 404)

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 200)

    def test_ventilator_delete(self):
        """Test for ventilator delete"""

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.delete("/project/room/SALA/ventilator/1/")

        self.assertEqual(response.status_code, 204)

    def test_ventilator_patch(self):
        """Test for ventilator patch"""
        # REVISAR

    def test_ventilator_add_ts(self):
        """Test for ventilator timestamp add"""

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.post("/project/room/SALA/ventilator/1/addTs/")

        self.assertEqual(response.status_code, 201)

    def test_ventilator_activity(self):
        """Test for ventilator activity"""

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))

        response = self.client.get("/project/room/SALA/ventilator/1/activity/")

        self.assertEqual(response.status_code, 200)

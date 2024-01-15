""" Test for views_puerta.py """

from django.test import TestCase, Client
from ..models import Room, RoomPeople
from ..models import RoomTemperature, RoomCO2


class InfoTests(TestCase):
    """Test class for ventana"""

    def setUp(self):
        """Set up"""
        self.client = Client()
        Room.objects.create(name="SALA", size=60)

    def test_room_people(self):
        "Test for room people"

        response = self.client.get("/project/room/SALA/people/")

        self.assertEqual(response.status_code, 404)

        RoomPeople.objects.create(room=Room.objects.get(name="SALA"), people=1)

        response = self.client.get("/project/room/SALA/people/")

        self.assertEqual(response.status_code, 200)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)

    def test_room_last_10_people(self):
        "Test for room last 10 people"

        response = self.client.get("/project/room/SALA/people/last10/")

        self.assertEqual(response.status_code, 404)

        RoomPeople.objects.create(room=Room.objects.get(name="SALA"), people=15)

        response = self.client.get("/project/room/SALA/people/last10/")

        self.assertEqual(response.status_code, 200)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)


    def test_room_add_people(self):
        "Test for room add people"

        data = {"people": 15}

        response = self.client.post(
            "/project/room/SALA/people/add/",
            data=data,
        )

        self.assertEqual(response.status_code, 200)

        room_people = RoomPeople.objects.get(room=Room.objects.get(name="SALA"))
        self.assertEqual(room_people.people, 15)

        response = self.client.post(
            "/project/room/NOEXISTE/people/add/",
            data=data,
        )

        self.assertEqual(response.status_code, 404)


    def test_room_temperature(self):
        "Test for room temperature"

        response = self.client.get("/project/room/SALA/temperature/")

        self.assertEqual(response.status_code, 404)

        RoomTemperature.objects.create(
            room=Room.objects.get(name="SALA"), temperature=1
        )

        response = self.client.get("/project/room/SALA/temperature/")

        self.assertEqual(response.status_code, 200)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)

    def test_room_last_10_temperature(self):
        "Test for room last 10 temperature"

        response = self.client.get("/project/room/SALA/temperature/last10/")

        self.assertEqual(response.status_code, 404)

        RoomTemperature.objects.create(
            room=Room.objects.get(name="SALA"), temperature=15
        )

        response = self.client.get("/project/room/SALA/temperature/last10/")

        self.assertEqual(response.status_code, 200)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)

    def test_room_add_temperature(self):
        "Test for room add temperature"

        data = {"temperature": 15}

        response = self.client.post(
            "/project/room/SALA/temperature/add/",
            data=data,
        )

        self.assertEqual(response.status_code, 200)

        room_temperature = RoomTemperature.objects.get(
            room=Room.objects.get(name="SALA")
        )
        self.assertEqual(room_temperature.temperature, 15)

        # Forzar 404
        response = self.client.post(
            "/project/room/NOEXISTE/temperature/add/",
            data=data,
        )

        self.assertEqual(response.status_code, 404)

    def test_room_co2(self):
        "Test for room co2"

        response = self.client.get("/project/room/SALA/co2/")

        self.assertEqual(response.status_code, 404)

        RoomCO2.objects.create(room=Room.objects.get(name="SALA"), co2=1)

        response = self.client.get("/project/room/SALA/co2/")

        self.assertEqual(response.status_code, 200)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)

    def test_room_last_10_co2(self):
        "Test for room last 10 co2"

        response = self.client.get("/project/room/SALA/co2/last10/")

        self.assertEqual(response.status_code, 404)

        RoomCO2.objects.create(room=Room.objects.get(name="SALA"), co2=15)

        response = self.client.get("/project/room/SALA/co2/last10/")

        self.assertEqual(response.status_code, 200)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 204)

        response = self.client.delete("/project/room/SALA/")

        self.assertEqual(response.status_code, 404)

    def test_room_add_co2(self):
        "Test for room add co2"

        # Prepare the data for the POST request
        data = {"co2": 15}

        # Use the Django test client to simulate a POST request
        response = self.client.post(
            "/project/room/SALA/co2/add/",
            data=data,
        )

        # Check if the response is as expected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"ok": "ok"})

        # Check if RoomCO2 object is created with the correct values
        room_co2 = RoomCO2.objects.get(room=Room.objects.get(name="SALA"))
        self.assertEqual(room_co2.co2, 15)

        # Forzar 404
        response = self.client.post(
            "/project/room/NOEXISTE/co2/add/",
            data=data,
        )

        self.assertEqual(response.status_code, 404)

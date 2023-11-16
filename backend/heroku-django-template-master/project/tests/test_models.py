from django.test import TestCase
from ..models import Room

class ModelTests(TestCase):
    def setUp(self):
        Room.objects.create(name="SALA", size=60)

    def test_room_create(self):
        room = Room.objects.get(name="SALA")
        self.assertEqual(room.name, "SALA")
        self.assertEqual(room.size, 60)

    def test_room_change(self):
        room = Room.objects.get(name="SALA")
        room.name = "SALA2"
        room.size = 100
        self.assertEqual(room.name, "SALA2")
        self.assertEqual(room.size, 100)
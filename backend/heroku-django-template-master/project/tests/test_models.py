""" Test for models of the project """

from django.test import TestCase
from ..models import (
    RoomPeople,
    Room,
    Door,
    RoomCO2,
    RoomTemperature,
    Window,
    Ventilator,
    Light,
    VentilatorIsOn,
    LightIsOn,
    WindowOpen,
    DoorOpen,
)


class ModelTests(TestCase):
    """Test class for models of the project"""

    def setUp(self):
        """Set up"""
        Room.objects.create(name="SALA", size=60)
        Room.objects.create(name="SALA2", size=80)

        Ventilator.objects.create(id=1, room=Room.objects.get(name="SALA"))
        Light.objects.create(id=1, room=Room.objects.get(name="SALA"))
        Window.objects.create(id=1, room=Room.objects.get(name="SALA"))

        Door.objects.create(id=1)
        Door.objects.get(id=1).rooms.add(Room.objects.get(name="SALA"))
        Door.objects.get(id=1).rooms.add(Room.objects.get(name="SALA2"))

        RoomPeople.objects.create(people=2, room=Room.objects.get(name="SALA"))
        RoomTemperature.objects.create(
            temperature=15, room=Room.objects.get(name="SALA")
        )
        RoomCO2.objects.create(co2=700, room=Room.objects.get(name="SALA"))

        VentilatorIsOn.objects.create(ventilator=Ventilator.objects.get(id=1))
        LightIsOn.objects.create(light=Light.objects.get(id=1))
        WindowOpen.objects.create(window=Window.objects.get(id=1))
        DoorOpen.objects.create(door=Door.objects.get(id=1))

    def test_room_create(self):
        """Room create"""
        room = Room.objects.get(name="SALA")
        self.assertEqual(room.name, "SALA")
        self.assertEqual(room.size, 60)

    def test_room_change(self):
        """Room change"""
        room = Room.objects.get(name="SALA")
        room.name = "SALA1"
        room.size = 100
        self.assertEqual(room.name, "SALA1")
        self.assertEqual(room.size, 100)

    def test_ventilator_create(self):
        """Ventilator create"""
        ventilator = Ventilator.objects.get(id=1)
        self.assertEqual(ventilator.name, "Ventilator")
        self.assertEqual(ventilator.isOn, False)

    def test_ventilator_change(self):
        """Ventilator change"""
        ventilator = Ventilator.objects.get(id=1)
        ventilator.name = "Ventilator1"
        ventilator.isOn = True
        self.assertEqual(ventilator.name, "Ventilator1")
        self.assertEqual(ventilator.isOn, True)

    def test_light_create(self):
        """Light create"""
        light = Light.objects.get(id=1)
        self.assertEqual(light.name, "Light")
        self.assertEqual(light.isOn, False)

    def test_light_change(self):
        """Light change"""
        light = Light.objects.get(id=1)
        light.name = "Light1"
        light.isOn = True
        self.assertEqual(light.name, "Light1")
        self.assertEqual(light.isOn, True)

    def test_window_create(self):
        """Window create"""
        window = Window.objects.get(id=1)
        self.assertEqual(window.name, "Window")
        self.assertEqual(window.isOpen, False)

    def test_window_change(self):
        """Window change"""
        window = Window.objects.get(id=1)
        window.name = "Window1"
        window.isOpen = True
        self.assertEqual(window.name, "Window1")
        self.assertEqual(window.isOpen, True)

    def test_door_create(self):
        """Door create"""
        door = Door.objects.get(id=1)
        self.assertEqual(door.name, "Door")
        self.assertEqual(door.isOpen, False)
        self.assertEqual(door.bloqueada, False)

    def test_door_change(self):
        """Door change"""
        door = Door.objects.get(id=1)
        door.name = "Door1"
        door.isOpen = True
        door.bloqueada = True
        self.assertEqual(door.name, "Door1")
        self.assertEqual(door.isOpen, True)
        self.assertEqual(door.bloqueada, True)

""" Test for models of the project """

from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
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

        with self.assertRaises(ObjectDoesNotExist):
            _ = Room.objects.get(name="SALA3")

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

    def test_room_timestamps(self):
        "Get room timestamps"
        room = Room.objects.get(name="SALA")
        people = RoomPeople.objects.get(room=room)
        temperature = RoomTemperature.objects.get(room=room)
        co2 = RoomCO2.objects.get(room=room)
        self.assertLess(people.timestamp, timezone.now())
        self.assertLess(temperature.timestamp, timezone.now())
        self.assertLess(co2.timestamp, timezone.now())
        self.assertEqual(people.people, 2)
        self.assertEqual(temperature.temperature, 15)
        self.assertEqual(co2.co2, 700)

    def test_ventilator_timestamp(self):
        "Get ventilator timestamp"
        ventilator = Ventilator.objects.get(id=1)
        is_on = VentilatorIsOn.objects.get(ventilator=ventilator)
        self.assertLess(is_on.timestamp, timezone.now())
        self.assertEqual(is_on.isOn, False)

    def test_light_timestamp(self):
        "Get light timestamp"
        light = Light.objects.get(id=1)
        is_on = LightIsOn.objects.get(light=light)
        self.assertLess(is_on.timestamp, timezone.now())
        self.assertEqual(is_on.isOn, False)

    def test_window_timestamp(self):
        "Get window timestamp"
        window = Window.objects.get(id=1)
        is_open = WindowOpen.objects.get(window=window)
        self.assertLess(is_open.timestamp, timezone.now())
        self.assertEqual(is_open.isOpen, False)

    def test_door_timestamp(self):
        "Get door timestamp"
        door = Door.objects.get(id=1)
        is_open = DoorOpen.objects.get(door=door)
        self.assertLess(is_open.timestamp, timezone.now())
        self.assertEqual(is_open.isOpen, False)

    def test_delete_cascade(self):
        "Delete on cascade"
        room = Room.objects.get(name="SALA")
        room.delete()

        room2 = Room.objects.get(name="SALA2")
        room2.delete()

        with self.assertRaises(ObjectDoesNotExist):
            _ = Room.objects.get(name="SALA")
        with self.assertRaises(ObjectDoesNotExist):
            _ = Ventilator.objects.get(id=1)
        with self.assertRaises(ObjectDoesNotExist):
            _ = Light.objects.get(id=1)
        with self.assertRaises(ObjectDoesNotExist):
            _ = Window.objects.get(id=1)
        # with self.assertRaises(ObjectDoesNotExist):
        #  _ = Door.objects.get(id=1)

        people = RoomPeople.objects.all()
        self.assertEqual(len(people), 0)

        co2 = RoomCO2.objects.all()
        self.assertEqual(len(co2), 0)

        temperature = RoomTemperature.objects.all()
        self.assertEqual(len(temperature), 0)

        onv = VentilatorIsOn.objects.all()
        self.assertEqual(len(onv), 0)

        onl = LightIsOn.objects.all()
        self.assertEqual(len(onl), 0)

        openw = WindowOpen.objects.all()
        self.assertEqual(len(openw), 0)

        # opend = DoorOpen.objects.all()
        # self.assertEqual(len(opend), 0)

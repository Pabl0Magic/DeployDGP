""" Models for the project """

# from typing_extensions import Self
from django.utils import timezone
from django.db import models

# Create your models here.


class Room(models.Model):
    """Room model"""

    name = models.CharField(max_length=30, primary_key=True)
    size = models.FloatField()


class Ventilator(models.Model):
    """Ventilator model"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default="Ventilator")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    isOn = models.BooleanField(default=False)


class Light(models.Model):
    """Light model"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default="Light")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    isOn = models.BooleanField(default=False)


class Window(models.Model):
    """Window model"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default="Window")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    isOpen = models.BooleanField(default=False)


class Door(models.Model):
    """Door model"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default="Door")
    rooms = models.ManyToManyField(Room)
    bloqueada = models.BooleanField(default=False)
    isOpen = models.BooleanField(default=False)


class RoomPeople(models.Model):
    """Room people model"""

    timestamp = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    people = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        """Meta class for the model"""

        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "room"], name="unique_timestamp_room_combination"
            )
        ]


class RoomTemperature(models.Model):
    """Room temperature model"""

    timestamp = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    temperature = models.FloatField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        """Meta class for the model"""

        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "room"],
                name="unique_timestamp_room_temperature_combination",
            )
        ]


class RoomCO2(models.Model):
    """Room CO2 model"""

    timestamp = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    co2 = models.FloatField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        """Meta class for the model"""

        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "room"],
                name="unique_timestamp_room_co2_combination",
            )
        ]


class VentilatorIsOn(models.Model):
    """Ventilator is on model"""

    timestamp = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    isOn = models.BooleanField(default=False)
    ventilator = models.ForeignKey(Ventilator, on_delete=models.CASCADE)

    class Meta:
        """Meta class for the model"""

        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "ventilator"],
                name="unique_timestamp_ventilator_combination",
            )
        ]


class LightIsOn(models.Model):
    """Light is on model"""

    timestamp = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    isOn = models.BooleanField(default=False)
    light = models.ForeignKey(Light, on_delete=models.CASCADE)

    class Meta:
        """Meta class for the model"""

        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "light"], name="unique_timestamp_light_combination"
            )
        ]


class WindowOpen(models.Model):
    """Window open model"""

    timestamp = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    isOpen = models.BooleanField(default=False)
    window = models.ForeignKey(Window, on_delete=models.CASCADE)

    class Meta:
        """Meta class for the model"""

        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "window"],
                name="unique_timestamp_window_combination",
            )
        ]


class DoorOpen(models.Model):
    """Door open model"""

    timestamp = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    isOpen = models.BooleanField(default=False)
    door = models.ForeignKey(Door, on_delete=models.CASCADE)

    class Meta:
        """Meta class for the model"""

        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "door"], name="unique_timestamp_door_combination"
            )
        ]


class UploadedFile(models.Model):
    """Uploaded file model"""

    file = models.FileField()

#from typing_extensions import Self
from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    size = models.FloatField()


class Ventilator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default='Ventilator')
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    isOn = models.BooleanField(default=False)


class Light(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default='Light')
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    isOn = models.BooleanField(default=False)


class Window(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default='Window')
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    isOpen = models.BooleanField(default=False)


class Door(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, default='Door')
    rooms = models.ManyToManyField(Room)
    bloqueada = models.BooleanField(default=False)
    isOpen = models.BooleanField(default=False)


class RoomPeople(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    people = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'room'], name='unique_timestamp_room_combination')]


class RoomTemperature(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'room'], name='unique_timestamp_room_temperature_combination')]


class RoomCO2(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    co2 = models.FloatField()
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'room'], name='unique_timestamp_room_co2_combination')]


class VentilatorIsOn(models.Model):
    timestamp = models.DateTimeField() #auto_now_add=True
    isOn = models.BooleanField()
    ventilator = models.ForeignKey(Ventilator, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'ventilator'], name='unique_timestamp_ventilator_combination')]


class LightIsOn(models.Model):
    timestamp = models.DateTimeField() #auto_now_add=True
    isOn = models.BooleanField()
    light = models.ForeignKey(Light, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'light'], name='unique_timestamp_light_combination')]


class WindowOpen(models.Model):
    timestamp = models.DateTimeField() #auto_now_add=True
    isOpen = models.BooleanField()
    window = models.ForeignKey(Window, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'window'], name='unique_timestamp_window_combination')]


class DoorOpen(models.Model):
    timestamp = models.DateTimeField() #auto_now_add=True
    isOpen = models.BooleanField()
    door = models.ForeignKey(Door, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'door'], name='unique_timestamp_door_combination')]


class UploadedFile(models.Model):
    file = models.FileField()
    
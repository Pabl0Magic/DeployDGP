from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    size = models.FloatField()


class Ventilator(models.Model):
    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.SET_DEFAULT)


class Window(models.Model):
    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.SET_DEFAULT)


class Door(models.Model):
    id = models.BigAutoField(primary_key=True)
    rooms = models.ManyToManyField(Room)


class PeopleInRoom(models.Model):
    timestamp = models.DateTimeField()
    NOPeopleInRoom = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.SET_DEFAULT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'room'], name='unique_timestamp_room_combination')]


class VentilatorIsOn(models.Model):
    timestamp = models.DateTimeField()
    isOn = models.BooleanField()
    ventilator = models.ForeignKey(Ventilator, on_delete=models.SET_DEFAULT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'ventilator'], name='unique_timestamp_ventilator_combination')]


class WindowOpen(models.Model):
    timestamp = models.DateTimeField()
    isOpen = models.BooleanField()
    window = models.ForeignKey(Window, on_delete=models.SET_DEFAULT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'window'], name='unique_timestamp_window_combination')]


class DoorOpen(models.Model):
    timestamp = models.DateTimeField()
    isOpen = models.BooleanField()
    door = models.ForeignKey(Door, on_delete=models.SET_DEFAULT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'door'], name='unique_timestamp_door_combination')]

class UploadedFile(models.Model):
    file = models.FileField()
    
from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    size = models.FloatField()
    co2 = models.FloatField(default=700)
    temperatura = models.FloatField(default=20)
    luz = models.BooleanField(default=False)


class Ventilator(models.Model):
    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)


class Window(models.Model):
    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)


class Door(models.Model):
    id = models.BigAutoField(primary_key=True)
    rooms = models.ManyToManyField(Room)
    bloqueada = models.BooleanField(default=False)


class PeopleInRoom(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    NOPeopleInRoom = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'room'], name='unique_timestamp_room_combination')]


class VentilatorIsOn(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    isOn = models.BooleanField()
    ventilator = models.ForeignKey(Ventilator, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'ventilator'], name='unique_timestamp_ventilator_combination')]


class WindowOpen(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    isOpen = models.BooleanField()
    window = models.ForeignKey(Window, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'window'], name='unique_timestamp_window_combination')]


class DoorOpen(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    isOpen = models.BooleanField()
    door = models.ForeignKey(Door, on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['timestamp', 'door'], name='unique_timestamp_door_combination')]


class UploadedFile(models.Model):
    file = models.FileField()
    
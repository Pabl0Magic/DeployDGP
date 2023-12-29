""" Admin page for the project """

from django.contrib import admin
from .models import DoorOpen, Room, Ventilator, VentilatorIsOn, Window, Door, WindowOpen

# Register your models here.
admin.site.register(Room)
admin.site.register(Ventilator)
admin.site.register(Window)
admin.site.register(Door)
admin.site.register(DoorOpen)
admin.site.register(VentilatorIsOn)
admin.site.register(WindowOpen)

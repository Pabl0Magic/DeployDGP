from django.contrib import admin
from .models import Room, Ventilator, Window, Door 
# Register your models here.
admin.site.register(Room)
admin.site.register(Ventilator)
admin.site.register(Window)
admin.site.register(Door)

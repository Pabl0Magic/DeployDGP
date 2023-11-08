from rest_framework import serializers
from .models import Room, Door, Window

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

class DoorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Door
        fields = '__all__'


class WindowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Window
        fields = '__all__'
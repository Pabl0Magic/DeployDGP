from rest_framework import serializers
from .models import Room, Door

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

class DoorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Door
        fields = '__all__'
from rest_framework import serializers
from .models import Room, Door, Ventilator, Window, Light

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


class LightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Light
        fields = '__all__'


class VentilatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ventilator
        fields = '__all__'
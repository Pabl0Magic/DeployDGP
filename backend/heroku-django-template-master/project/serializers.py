""" Serializers file to work with the models """

from rest_framework import serializers
from .models import Room, Door, Ventilator, Window, Light


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for Room Model"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for the serializer"""

        model = Room
        fields = "__all__"


class DoorSerializer(serializers.ModelSerializer):
    """Serializer for Door Model"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for the serializer"""

        model = Door
        fields = "__all__"


class WindowSerializer(serializers.ModelSerializer):
    """Serializer for Window Model"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for the serializer"""

        model = Window
        fields = "__all__"


class LightSerializer(serializers.ModelSerializer):
    """Serializer for Light Model"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for the serializer"""

        model = Light
        fields = "__all__"


class VentilatorSerializer(serializers.ModelSerializer):
    """Serializer for Ventilator Model"""

    class Meta:
        """Meta class for the serializer"""

        model = Ventilator
        fields = "__all__"

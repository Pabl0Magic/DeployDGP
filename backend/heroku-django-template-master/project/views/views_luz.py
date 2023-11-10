from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import Room, Light, LightIsOn
from ..forms import RoomForm, FileUploadForm
from ..serializers import LightSerializer

from django.views import View, generic
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime

import pandas as pd

@api_view(['GET'])
def get_all_lights(request, room_name):
    lights = Light.objects.filter(room__pk=room_name)  # Retrieve all lights from a room from the database
    lights_serializer = LightSerializer(lights, many=True)  # Serialize all lights

    if lights:
        return Response(lights_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No lights found", status=status.HTTP_404_NOT_FOUND)


class LightView(APIView):
    def get(self, request, room_name, light_id=None, format=None):
        if light_id:
            light = get_object_or_404(Light, id=light_id)
            light_ser = LightSerializer(light)
            return Response(light_ser.data, status=status.HTTP_200_OK)
        else:
            return Response("Please provide a light id", status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, format=None, room_name=None):
        light_ser = LightSerializer(data=request.data)

        if light_ser.is_valid():
            light_instance = light_ser.save()

            room = Room.objects.get(name=room_name)

            light_instance.room = room

            LightIsOn.objects.create(light=light_instance, timestamp=datetime.now())

            return Response(light_ser.data, status=status.HTTP_201_CREATED)
        
        return Response(light_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, room_name, light_id, format=None):
        try:
            light = Light.objects.get(id=light_id)
            light.delete()
            return Response(f"Light '{light_id}' deleted successfully", status=status.HTTP_204_NO_CONTENT)
        except Light.DoesNotExist:
            return Response("Light does not exist", status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, room_name, light_id, format=None):
        try:
            light = Light.objects.get(id=light_id)
            light_serializer = LightSerializer(light, data=request.data, partial=True)

            if light_serializer.is_valid():
                light_serializer.save()
                return Response(light_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(light_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Light.DoesNotExist:
            return Response("Light does not exist", status=status.HTTP_404_NOT_FOUND)    


class LightIsOnView(APIView):
    def post(self, request, room_name, light_id, format=None):
        try:
            light_instance = Light.objects.get(id=light_id)

            timestamp = datetime.now()
            isOn = request.data.get('isOn', False)

            light_instance.isOn = isOn
            light_instance.save()
            
            light_open_instance = LightIsOn.objects.create(light=light_instance, timestamp=timestamp, isOn=isOn)
            
            return Response({"id": light_instance.id, "timestamp": timestamp, "isOn": isOn}, status=status.HTTP_201_CREATED)
        except Light.DoesNotExist:
            return Response("Light does not exist", status=status.HTTP_404_NOT_FOUND)  


@api_view(['GET'])
def get_recent_light_activity(request, room_name, light_id):
    try:
        light = Light.objects.get(id=light_id)

        light = get_object_or_404(Light, id=light.id)
        light_ons = LightIsOn.objects.filter(
            light__id=light.id
        ).order_by('light', 'timestamp')
        
        current_activities = []

        for light_on in light_ons:
            current_activities.append({"isOn": light_on.isOn, "timestamp": light_on.timestamp})

        return Response({"id": light.id, "name": light.name, "activities": current_activities})
            
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

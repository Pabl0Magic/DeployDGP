from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import DoorOpen, RoomPeople, Room, Door, RoomCO2, RoomTemperature, Window, Ventilator
from ..forms import RoomForm, FileUploadForm
from ..serializers import DoorSerializer

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
def get_all_doors(request, room_name):
    doors = Door.objects.filter(rooms__pk=room_name)  # Retrieve all doors from a room from the database
    door_serializer = DoorSerializer(doors, many=True)  # Serialize all doors

    if doors:
        return Response(door_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No doors found", status=status.HTTP_404_NOT_FOUND)


class DoorView(APIView):
    def get(self, request, door_id=None, format=None):
        if door_id:
            door = get_object_or_404(Door, id=door_id)
            door_ser = DoorSerializer(door)
            return Response(door_ser.data, status=status.HTTP_200_OK)
        else:
            return Response("Please provide a door id", status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, format=None, room_name=None):
        door_ser = DoorSerializer(data=request.data)

        if door_ser.is_valid():
            door_instance = door_ser.save()

            room = Room.objects.get(name=room_name)

            door_instance.rooms.add(room)

            DoorOpen.objects.create(door=door_instance, timestamp=datetime.now())

            return Response(door_ser.data, status=status.HTTP_201_CREATED)
        
        return Response(door_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, door_id, format=None):
        try:
            door = Door.objects.get(id=door_id)
            door.delete()
            return Response(f"Door '{door_id}' deleted successfully", status=status.HTTP_204_NO_CONTENT)
        except Door.DoesNotExist:
            return Response("Door does not exist", status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, door_id, format=None):
        try:
            door = Door.objects.get(id=door_id)
            door_serializer = DoorSerializer(door, data=request.data, partial=True)

            if door_serializer.is_valid():
                door_serializer.save()
                return Response(door_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(door_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Door.DoesNotExist:
            return Response("Door does not exist", status=status.HTTP_404_NOT_FOUND)    
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import DoorOpen, RoomPeople, Room, Door, RoomCO2, RoomTemperature, VentilatorIsOn, Window, Ventilator
from ..forms import RoomForm, FileUploadForm
from ..serializers import DoorSerializer, VentilatorSerializer

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

from datetime import datetime, timedelta

import pandas as pd

@api_view(['GET'])
def get_all_ventilators(request, room_name):
    ventilators = Ventilator.objects.filter(room__pk=room_name) 
    ventilator_serializer = VentilatorSerializer(ventilators, many=True)

    if ventilators:
        return Response(ventilator_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No ventilators found", status=status.HTTP_404_NOT_FOUND)


class VentilatorView(APIView):
    def get(self, request, room_name, ventilator_id, format=None):
        if ventilator_id:
            ventilator = get_object_or_404(Ventilator, id=ventilator_id)
            ventilator_ser = VentilatorSerializer(ventilator)
            return Response(ventilator_ser.data, status=status.HTTP_200_OK)
        else:
            return Response("Please provide a ventilator id", status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, room_name, format=None):
        ventilator_ser = VentilatorSerializer(data=request.data)

        if ventilator_ser.is_valid():
            ventilator_instance = ventilator_ser.save()

            room = Room.objects.get(name=room_name)

            ventilator_instance.room = room

            VentilatorIsOn.objects.create(ventilator=ventilator_instance, timestamp=datetime.now())

            return Response(ventilator_ser.data, status=status.HTTP_201_CREATED)
        
        return Response(ventilator_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, room_name, ventilator_id, format=None):
        try:
            ventilator = Ventilator.objects.get(id=ventilator_id)
            ventilator.delete()
            return Response(f"Ventilator '{ventilator_id}' deleted successfully", status=status.HTTP_204_NO_CONTENT)
        except Ventilator.DoesNotExist:
            return Response("Ventilator does not exist", status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, room_name, ventilator_id, format=None):
        try:
            ventilator = Ventilator.objects.get(id=ventilator_id)
            ventilator_serializer = VentilatorSerializer(ventilator, data=request.data, partial=True)

            if ventilator_serializer.is_valid():
                ventilator_serializer.save()
                return Response(ventilator_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(ventilator_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Ventilator.DoesNotExist:
            return Response("Ventilator does not exist", status=status.HTTP_404_NOT_FOUND)  


class VentilatorIsOnView(APIView):
    def post(self, request, room_name, ventilator_id, format=None):
        try:
            ventilator_instance = Ventilator.objects.get(id=ventilator_id)

            timestamp = datetime.now()
            isOn = request.data.get('isOn', False)

            ventilator_instance.isOn = isOn
            ventilator_instance.save()
            
            ventilator_on_instance = VentilatorIsOn.objects.create(ventilator=ventilator_instance, timestamp=timestamp, isOn=isOn)
            
            return Response({"id": ventilator_instance.id, "timestamp": timestamp, "isOn": isOn}, status=status.HTTP_201_CREATED)
        except Ventilator.DoesNotExist:
            return Response("Ventilator does not exist", status=status.HTTP_404_NOT_FOUND)  
        

@api_view(['GET'])
def get_recent_ventilator_activity(request, room_name, ventilator_id):
    try:
        ventilator = Ventilator.objects.get(id=ventilator_id)

        ventilator = get_object_or_404(Ventilator, id=ventilator.id)
        ventilator_ons = VentilatorIsOn.objects.filter(
            ventilator__id=ventilator.id
        ).order_by('ventilator', 'timestamp')
        
        current_activities = []

        for ventilator_on in ventilator_ons:
            current_activities.append({"isOn": ventilator_on.isOn, "timestamp": ventilator_on.timestamp})

        return Response({"id": ventilator.id, "name": ventilator.name, "activities": current_activities})
            
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

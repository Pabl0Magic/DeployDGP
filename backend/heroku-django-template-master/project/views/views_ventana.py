from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import Window, WindowOpen, Room
from ..forms import RoomForm, FileUploadForm
from ..serializers import WindowSerializer

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
def get_all_windows(request, room_name):
    windows = Window.objects.filter(room__pk=room_name)  # Retrieve all windows from a room from the database
    windows_serializer = WindowSerializer(windows, many=True)  # Serialize all windows

    if windows:
        return Response(windows_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No windows found", status=status.HTTP_404_NOT_FOUND)


class WindowView(APIView):
    def get(self, request, window_id=None, format=None):
        if window_id:
            window = get_object_or_404(Window, id=window_id)
            window_ser = WindowSerializer(window)
            return Response(window_ser.data, status=status.HTTP_200_OK)
        else:
            return Response("Please provide a window id", status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, format=None, room_name=None):
        window_ser = WindowSerializer(data=request.data)

        if window_ser.is_valid():
            window_instance = window_ser.save()

            room = Room.objects.get(name=room_name)

            window_instance.room = room

            WindowOpen.objects.create(window=window_instance, timpestamp=datetime.now())

            return Response(window_ser.data, status=status.HTTP_201_CREATED)
        
        return Response(window_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, window_id, format=None):
        try:
            window = Window.objects.get(id=window_id)
            window.delete()
            return Response(f"Window '{window_id}' deleted successfully", status=status.HTTP_204_NO_CONTENT)
        except Window.DoesNotExist:
            return Response("Window does not exist", status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, window_id, format=None):
        try:
            window = Window.objects.get(id=window_id)
            window_serializer = WindowSerializer(window, data=request.data, partial=True)

            if window_serializer.is_valid():
                window_serializer.save()
                return Response(window_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(window_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Window.DoesNotExist:
            return Response("Window does not exist", status=status.HTTP_404_NOT_FOUND)    
    
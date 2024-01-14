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


@api_view(["GET"])
def get_all_windows(request, room_name):
    windows = Window.objects.filter(
        room__pk=room_name
    )  # Retrieve all windows from a room from the database
    windows_serializer = WindowSerializer(windows, many=True)  # Serialize all windows

    if windows:
        return Response(windows_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No windows found", status=status.HTTP_404_NOT_FOUND)


class WindowView(APIView):
    def get(self, request, room_name, window_id=None, format=None):
        if window_id:
            window = get_object_or_404(Window, id=window_id)
            window_ser = WindowSerializer(window)
            return Response(window_ser.data, status=status.HTTP_200_OK)
        else:
            return Response(
                "Please provide a window id", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, format=None, room_name=None):
        window_ser = WindowSerializer(data=request.data)

        if window_ser.is_valid():
            window_instance = window_ser.save()

            room = Room.objects.get(name=room_name)

            window_instance.room = room

            WindowOpen.objects.create(window=window_instance, timestamp=datetime.now())

            return Response(window_ser.data, status=status.HTTP_201_CREATED)

        return Response(window_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, room_name, window_id, format=None):
        try:
            window = Window.objects.get(id=window_id)
            window.delete()
            return Response(
                f"Window '{window_id}' deleted successfully",
                status=status.HTTP_204_NO_CONTENT,
            )
        except Window.DoesNotExist:
            return Response("Window does not exist", status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, room_name, window_id, format=None):
        try:
            window = Window.objects.get(id=window_id)
            window_serializer = WindowSerializer(
                window, data=request.data, partial=True
            )

            if window_serializer.is_valid():
                window_serializer.save()
                return Response(window_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    window_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except Window.DoesNotExist:
            return Response("Window does not exist", status=status.HTTP_404_NOT_FOUND)


class WindowOpenView(APIView):
    def post(self, request, room_name, window_id, format=None):
        try:
            window_instance = Window.objects.get(id=window_id)

            timestamp = datetime.now()
            isOpen = request.data.get("isOpen", False)

            window_instance.isOpen = isOpen
            window_instance.save()

            window_open_instance = WindowOpen.objects.create(
                window=window_instance, timestamp=timestamp, isOpen=isOpen
            )

            return Response(
                {"id": window_instance.id, "timestamp": timestamp, "isOpen": isOpen},
                status=status.HTTP_201_CREATED,
            )
        except Window.DoesNotExist:
            return Response("Window does not exist", status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def get_recent_window_activity(request, room_name, window_id):
    try:
        window = get_object_or_404(Window, id=window_id)
        window_opens = WindowOpen.objects.filter(window__id=window.id).order_by(
            "window", "timestamp"
        )

        current_activities = []

        for window_open in window_opens:
            current_activities.append(
                {"isOpen": window_open.isOpen, "timestamp": window_open.timestamp}
            )

        return Response(
            {"id": window.id, "name": window.name, "activities": current_activities}
        )

    except Exception as e:
        return Response(
            {"error": f"An error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

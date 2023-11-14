from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import (
    RoomPeople,
    Room,
    Door,
    RoomCO2,
    RoomTemperature,
    Window,
    Ventilator,
    Light,
)
from ..forms import RoomForm, FileUploadForm
from ..serializers import RoomSerializer

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

import pandas as pd
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        )
    )
)


def index(request):
    return render(request, "upload.html")


@require_POST
def import_excel(request):
    if "file" in request.FILES:
        excel_file = request.FILES["file"]

        if isinstance(excel_file, InMemoryUploadedFile):
            try:
                data = pd.read_excel(excel_file)

                if "Room" in data:
                    room_data = data["Room"]
                    for index, row in room_data.iterrows():
                        Room.objects.create(name=row["roomName"], size=row["roomSize"])

                if "Door" in data:
                    door_data = data["Door"]
                    for index, row in door_data.iterrows():
                        Door.objects.create(id=row["ID"])

                if "Window" in data:
                    window_data = data["Window"]
                    for index, row in window_data.iterrows():
                        room_id = row["roomID"]

                        try:
                            room = Room.objects.get(name=room_id)
                            Window.objects.create(id=row["ID"], room=room)
                        except Room.DoesNotExist:
                            print(f"Room with name {room_id} not found.")
                        except Exception as e:
                            print(f"Error creating Window: {str(e)}")

                if "Ventilator" in data:
                    ventilator_data = data["Ventilator"]
                    for index, row in ventilator_data.iterrows():
                        room_id = row["roomID"]

                        try:
                            room = Room.objects.get(name=room_id)
                            Ventilator.objects.create(id=row["ID"], room=room)
                        except Room.DoesNotExist:
                            print(f"Room with name {room_id} not found.")
                        except Exception as e:
                            print(f"Error creating Ventilator: {str(e)}")

                return JsonResponse({"message": "Data imported successfully"})

            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "No file found in the request"}, status=400)


@require_POST
def export_data(request):
    if "file" in request.FILES:
        file_path = os.path.join(BASE_DIR, "room_data.csv")

        try:
            rooms = Room.objects.all()
            room_lists = []

            for room in rooms:
                doors = Door.objects.filter(rooms__pk=room.name)
                door_list = []
                for door in doors:
                    door_list.append(door.name)

                windows = Window.objects.filter(room__pk=room.name)
                window_list = []
                for window in windows:
                    window_list.append(window.name)

                ligths = Light.objects.filter(room__pk=room.name)
                ligths_list = []
                for light in ligths:
                    ligths_list.append(light.name)

                ventilators = Ventilator.objects.filter(room__pk=room.name)
                ventilator_list = []
                for ventilator in ventilators:
                    ventilator_list.append(ventilator.name)

                room_lists.append(
                    (
                        room.name,
                        room.size,
                        door_list,
                        window_list,
                        ligths_list,
                        ventilator_list,
                    )
                )

            df = pd.DataFrame({"Rooms": room_lists})
            df.to_csv(file_path, index=False)

            return JsonResponse({"message": "Data exported completed successfully"})

        except Exception as e:
            return JsonResponse({"error": "Data export failed"}, status=400)


class Home(generic.ListView):
    # Comentario generico
    model = Room
    template_name = "home.html"


@api_view(["GET"])
def get_all_rooms(request):
    rooms = Room.objects.all()  # Retrieve all rooms from the database
    room_serializer = RoomSerializer(rooms, many=True)  # Serialize all rooms

    if rooms:
        return Response(room_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No rooms found", status=status.HTTP_404_NOT_FOUND)


class RoomView(APIView):
    def get(self, request, room_name=None, format=None):
        if room_name:
            room = get_object_or_404(Room, name=room_name)
            room_ser = RoomSerializer(room)
            return Response(room_ser.data, status=status.HTTP_200_OK)
        else:
            return Response(
                "Please provide a room name", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, format=None):
        room_ser = RoomSerializer(data=request.data)

        if room_ser.is_valid():
            room_instance = room_ser.save()

            RoomPeople.objects.create(room=room_instance, people=0)
            RoomTemperature.objects.create(room=room_instance, temperature=20)
            RoomCO2.objects.create(room=room_instance, co2=700)

            return Response(room_ser.data, status=status.HTTP_201_CREATED)

        return Response(room_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, room_name, format=None):
        try:
            room = Room.objects.get(name=room_name)
            room.delete()
            return Response(
                f"Room '{room_name}' deleted successfully",
                status=status.HTTP_204_NO_CONTENT,
            )
        except Room.DoesNotExist:
            return Response("Room does not exist", status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, room_name, format=None):
        try:
            room = Room.objects.get(name=room_name)
            room_serializer = RoomSerializer(room, data=request.data, partial=True)

            if room_serializer.is_valid():
                room_serializer.save()
                return Response(room_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    room_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except Room.DoesNotExist:
            return Response("Room does not exist", status=status.HTTP_404_NOT_FOUND)

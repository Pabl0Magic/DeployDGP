from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import Room, Door, Window, Ventilator
from ..forms import RoomForm, FileUploadForm
from ..serializers import RoomSerializer

from django.views import View, generic
from django.views.decorators.http import require_POST
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import pandas as pd

def index(request):
	return render(request, 'upload.html')

@require_POST
def import_excel(request):
    if 'file' in request.FILES:
        excel_file = request.FILES['file']
        
        if isinstance(excel_file, InMemoryUploadedFile):
            try:
                data = pd.read_excel(excel_file)

                if 'Room' in data:
                    room_data = data['Room']
                    for index, row in room_data.iterrows():
                        Room.objects.create(name=row['roomName'], size=row['roomSize'])

                if 'Door' in data:
                      door_data = data['Door']
                      for index, row in door_data.iterrows():
                        Door.objects.create(id=row['ID'])

                if 'Window' in data:
                    window_data = data['Window']
                    for index, row in window_data.iterrows():
                        room_id = row['roomID']

                        try:
                            room = Room.objects.get(name=room_id) 
                            Window.objects.create(id=row['ID'], room=room)
                        except Room.DoesNotExist:
                            print(f"Room with name {room_id} not found.")
                        except Exception as e:
                            print(f"Error creating Window: {str(e)}")

                if 'Ventilator' in data:
                    ventilator_data = data['Ventilator']
                    for index, row in ventilator_data.iterrows():
                        room_id = row['roomID']

                        try:
                            room = Room.objects.get(name=room_id)  
                            Ventilator.objects.create(id=row['ID'], room=room)
                        except Room.DoesNotExist:
                            print(f"Room with name {room_id} not found.")
                        except Exception as e:
                            print(f"Error creating Ventilator: {str(e)}")

                return JsonResponse({'message': 'Data imported successfully'})

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'No file found in the request'}, status=400)

class Home(generic.ListView):

    model = Room
    template_name = 'home.html'

class RoomCreateView(APIView):
    def post(self, request, format=None):
        roomSer = RoomSerializer(data=request.data)

        if roomSer.is_valid():
            roomSer.save()
            return Response(roomSer.data, status=status.HTTP_201_CREATED)
        return Response(roomSer.errors, status=status.HTTP_400_BAD_REQUEST)

"""class FileUploadView(View):
	def post(self, request):
		form = FileUploadForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return JsonResponse({'message': 'File uploaded succesfully'})
		else:
			return JsonResponse({'message': 'Error uploading file'}, staus=400)
		
		"""
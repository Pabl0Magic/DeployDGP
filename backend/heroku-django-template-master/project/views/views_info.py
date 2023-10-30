from django.views import View, generic
from django.views.decorators.http import require_POST
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Room, PeopleInRoom

def room_people_count(request, room_name):
  """try:
    room = Room.objects.get(name=room_name)
    latest_people_count = PeopleInRoom.objects.filter(room=room).latest('timestamp').NOPeopleInRoom
    return JsonResponse({'room': room_name, 'people_count': latest_people_count})
  
  except Room.DoesNotExist:
    return JsonResponse({'error': f'Room "{room_name}" not found'}, status=404)
  
  except PeopleInRoom.DoesNotExist:
    return JsonResponse({'error': f'No people count available for room "{room_name}"'}, status=404)"""
  
  try:
    room = Room.objects.get(name=room_name)
    people_count_in_room = room.NOPeopleInRoom
    return JsonResponse({'room': room_name, 'people_count': people_count_in_room})
  except Room.DoesNotExist:
    return JsonResponse({'error': f'Room "{room_name}" not found'}, status=404)


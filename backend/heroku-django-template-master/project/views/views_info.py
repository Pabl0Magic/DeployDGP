from django.http import JsonResponse

from ..models import Room, PeopleInRoom, RoomCO2, RoomTemperature

def room_people(request, room_name):
  try:
    room = Room.objects.get(name=room_name)
    people_count = PeopleInRoom.objects.filter(room=room).latest('timestamp').NOPeopleInRoom
    timestamp = PeopleInRoom.objects.filter(room=room).latest('timestamp').timestamp
    return JsonResponse({'room': room_name, 'people_count': people_count, 'timestamp': timestamp})

  except Room.DoesNotExist:
    return JsonResponse({'error': f'Room "{room_name}" not found'}, status=404)

  except PeopleInRoom.DoesNotExist:
    return JsonResponse({'error': f'No people count available for room "{room_name}"'}, status=404)

def room_temperature(request, room_name):
  try:
    room = Room.objects.get(name=room_name)
    temperature = RoomTemperature.objects.filter(room=room).latest('timestamp').temperature
    timestamp = PeopleInRoom.objects.filter(room=room).latest('timestamp').timestamp
    return JsonResponse({'room': room_name, 'temperature': temperature, 'timestamp': timestamp})

  except Room.DoesNotExist:
    return JsonResponse({'error': f'Room "{room_name}" not found'}, status=404)

  except RoomTemperature.DoesNotExist:
    return JsonResponse({'error': f'No temperature record available for room "{room_name}"'}, status=404)

def room_co2(request, room_name):
  try:
    room = Room.objects.get(name=room_name)
    co2 = RoomCO2.objects.filter(room=room).latest('timestamp').co2
    timestamp = PeopleInRoom.objects.filter(room=room).latest('timestamp').timestamp
    return JsonResponse({'room': room_name, 'co2': co2, 'timestamp': timestamp})

  except Room.DoesNotExist:
    return JsonResponse({'error': f'Room "{room_name}" not found'}, status=404)

  except RoomTemperature.DoesNotExist:
    return JsonResponse({'error': f'No CO2 record available for room "{room_name}"'}, status=404)
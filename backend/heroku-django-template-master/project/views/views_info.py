from django.http import JsonResponse
from django.core import serializers
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from ..models import Room, RoomPeople, RoomCO2, RoomTemperature


def room_people(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        people_count = RoomPeople.objects.filter(room=room).latest("timestamp").people
        timestamp = RoomPeople.objects.filter(room=room).latest("timestamp").timestamp
        return JsonResponse(
            {"room": room_name, "data": people_count, "timestamp": timestamp}
        )

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)

    except RoomPeople.DoesNotExist:
        return JsonResponse(
            {"error": f'No people count available for room "{room_name}"'}, status=404
        )


def room_last_10_people(request, room_name):
    try:
        room = Room.objects.get(name=room_name)

        people_entries = RoomPeople.objects.filter(room=room).order_by("-timestamp")[
            :10
        ]

        if people_entries:
            data = [
                {"timestamp": entry.timestamp, "value": entry.people}
                for entry in people_entries
            ]

            return JsonResponse({"room": room_name, "data": data})
        else:
            return JsonResponse(
                {"error": f'No people records available for room "{room_name}"'},
                status=404,
            )

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)


@csrf_exempt
@require_POST
def room_add_people(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        people_count = request.POST.get("people")

        print(people_count)

        room_people = RoomPeople.objects.create(room=room, people=people_count)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "people",
            {
                "type": "people.message",
                "people": str(room_people.people),
            },
        )

        return JsonResponse({"ok": "ok"})

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)

    except RoomPeople.DoesNotExist:
        return JsonResponse(
            {"error": f'No people count available for room "{room_name}"'}, status=404
        )


def room_temperature(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        temperature = (
            RoomTemperature.objects.filter(room=room).latest("timestamp").temperature
        )
        timestamp = (
            RoomTemperature.objects.filter(room=room).latest("timestamp").timestamp
        )
        return JsonResponse(
            {"room": room_name, "data": temperature, "timestamp": timestamp}
        )

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)

    except RoomTemperature.DoesNotExist:
        return JsonResponse(
            {"error": f'No temperature record available for room "{room_name}"'},
            status=404,
        )


def room_last_10_temperature(request, room_name):
    try:
        room = Room.objects.get(name=room_name)

        temperature_entries = RoomTemperature.objects.filter(room=room).order_by(
            "-timestamp"
        )[:10]

        if temperature_entries:
            data = [
                {"timestamp": entry.timestamp, "value": entry.temperature}
                for entry in temperature_entries
            ]

            return JsonResponse({"room": room_name, "data": data})
        else:
            return JsonResponse(
                {"error": f'No temperature records available for room "{room_name}"'},
                status=404,
            )

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)


@csrf_exempt
@require_POST
def room_add_temperature(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        temperature_count = request.POST.get("temperature")
        room_temperature = RoomTemperature.objects.create(
            room=room, temperature=temperature_count
        )

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "temperature",
            {
                "type": "temperature.message",
                "temperature": str(room_temperature.temperature),
            },
        )

        return JsonResponse({"ok": "ok"})

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)

    except RoomPeople.DoesNotExist:
        return JsonResponse(
            {"error": f'No temperature count available for room "{room_name}"'},
            status=404,
        )


def room_co2(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        co2 = RoomCO2.objects.filter(room=room).latest("timestamp").co2
        timestamp = RoomCO2.objects.filter(room=room).latest("timestamp").timestamp
        return JsonResponse({"room": room_name, "data": co2, "timestamp": timestamp})

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)

    except RoomCO2.DoesNotExist:
        return JsonResponse(
            {"error": f'No CO2 record available for room "{room_name}"'}, status=404
        )


def room_last_10_co2(request, room_name):
    try:
        room = Room.objects.get(name=room_name)

        co2_entries = RoomCO2.objects.filter(room=room).order_by("-timestamp")[:10]

        if co2_entries:
            data = [
                {"timestamp": entry.timestamp, "value": entry.co2}
                for entry in co2_entries
            ]

            return JsonResponse({"room": room_name, "data": data})
        else:
            return JsonResponse(
                {"error": f'No CO2 records available for room "{room_name}"'},
                status=404,
            )

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)


@csrf_exempt
@require_POST
def room_add_co2(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        co2_count = request.POST.get("co2")
        room_co2 = RoomCO2.objects.create(room=room, co2=co2_count)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "co2",
            {
                "type": "co2.message",
                "co2": str(room_co2.co2),
            },
        )

        return JsonResponse({"ok": "ok"})

    except Room.DoesNotExist:
        return JsonResponse({"error": f'Room "{room_name}" not found'}, status=404)

    except RoomPeople.DoesNotExist:
        return JsonResponse(
            {"error": f'No CO2 count available for room "{room_name}"'}, status=404
        )

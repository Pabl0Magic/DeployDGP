from .consumers.consumer_info import RoomPeopleConsumer, RoomTemperatureConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r"ws/room/people/(?P<room_name>\w+)/$", RoomPeopleConsumer.as_asgi()),
    re_path(r"ws/room/temperature/(?P<room_name>\w+)/$", RoomTemperatureConsumer.as_asgi()),
]
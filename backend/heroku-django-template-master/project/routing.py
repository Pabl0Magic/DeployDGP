""" Routing file to connect with frontend """

from django.urls import re_path
from .consumers.consumer_info import (
    RoomCO2Consumer,
    RoomPeopleConsumer,
    RoomTemperatureConsumer,
)

websocket_urlpatterns = [
    re_path(r"ws/room/people/(?P<room_name>\w+)/$", RoomPeopleConsumer.as_asgi()),
    re_path(
        r"ws/room/temperature/(?P<room_name>\w+)/$", RoomTemperatureConsumer.as_asgi()
    ),
    re_path(r"ws/room/co2/(?P<room_name>\w+)/$", RoomCO2Consumer.as_asgi()),
]

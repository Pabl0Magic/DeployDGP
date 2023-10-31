from .consumers.consumer_info import RoomPeopleConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r"ws/room/people/(?P<room_name>\w+)/$", RoomPeopleConsumer.as_asgi()),
]
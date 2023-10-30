from django.urls import path

from .views import views_sala, views_info

urlpatterns = [
    path('', views_sala.index, name='index'),
    path('home/', views_sala.Home.as_view(), name='home'),
    path('room/create', views_sala.RoomCreateView.as_view(), name='room-create'),
    path('room/<str:room_name>/people_count/', views_info.room_people_count, name='room-people-count'),
    path('room/<str:room_name>/temperature/', views_info.room_temperature, name='room-temperature'),
]
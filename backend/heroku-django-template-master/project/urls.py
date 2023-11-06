from django.urls import path

from .views import views_sala, views_info

urlpatterns = [
    path('', views_sala.index, name='index'),
    path('home/', views_sala.Home.as_view(), name='home'),
    path('room/create', views_sala.RoomView.as_view(), name='room-create'),
    path('room/<str:room_name>/', views_sala.RoomView.as_view(), name='room-get'),
    path('room/<str:room_name>/people/', views_info.room_people, name='room-people'),
    path('room/<str:room_name>/people/last10/', views_info.room_last_10_people, name='room-last-10-people'),
    path('room/<str:room_name>/people/add/', views_info.room_add_people, name='room-add-people'),
    path('room/<str:room_name>/temperature/', views_info.room_temperature, name='room-temperature'),
    path('room/<str:room_name>/temperature/last10/', views_info.room_last_10_temperature, name='room-last-10-temperature'),
    path('room/<str:room_name>/temperature/add/', views_info.room_add_temperature, name='room-add-temperature'),
    path('room/<str:room_name>/co2/', views_info.room_co2, name='room-co2'),
    path('room/<str:room_name>/co2/last10/', views_info.room_last_10_co2, name='room-last-10-co2'),
    path('room/<str:room_name>/co2/add/', views_info.room_add_co2, name='room-add-co2'),
]
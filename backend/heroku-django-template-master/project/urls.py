from django.urls import path

from .views import views_sala, views_info, views_puerta, views_ventana, views_luz

urlpatterns = [
    path('', views_sala.index, name='index'),
    path('home/', views_sala.Home.as_view(), name='home'),
    path('room/all/', views_sala.get_all_rooms, name='room-all'),
    path('room/create/', views_sala.RoomView.as_view(), name='room-create'),
    path('room/<str:room_name>/', views_sala.RoomView.as_view(), name='room'),
    path('room/<str:room_name>/people/', views_info.room_people, name='room-people'),
    path('room/<str:room_name>/people/last10/', views_info.room_last_10_people, name='room-last-10-people'),
    path('room/<str:room_name>/people/add/', views_info.room_add_people, name='room-add-people'),
    path('room/<str:room_name>/temperature/', views_info.room_temperature, name='room-temperature'),
    path('room/<str:room_name>/temperature/last10/', views_info.room_last_10_temperature, name='room-last-10-temperature'),
    path('room/<str:room_name>/temperature/add/', views_info.room_add_temperature, name='room-add-temperature'),
    path('room/<str:room_name>/co2/', views_info.room_co2, name='room-co2'),
    path('room/<str:room_name>/co2/last10/', views_info.room_last_10_co2, name='room-last-10-co2'),
    path('room/<str:room_name>/co2/add/', views_info.room_add_co2, name='room-add-co2'),
    path('room/<str:room_name>/door/all/', views_puerta.get_all_doors, name='door-all'),
    path('room/<str:room_name>/door/create/', views_puerta.DoorView.as_view(), name='door-create'),
    path('room/<str:room_name>/door/<str:door_id>/', views_puerta.DoorView.as_view(), name='door'),
    path('room/<str:room_name>/door/<str:door_id>/addTs/', views_puerta.DoorOpenView.as_view(), name='door-add-ts'),
    path('room/<str:room_name>/door/<str:door_id>/activity/', views_puerta.get_recent_door_activity, name='door-activity'),
    path('room/<str:room_name>/window/all/', views_ventana.get_all_windows, name='window-all'),
    path('room/<str:room_name>/window/create/', views_ventana.WindowView.as_view(), name='window-create'),
    path('room/<str:room_name>/window/<str:window_id>/', views_ventana.WindowView.as_view(), name='window'),
    path('room/<str:room_name>/window/<str:window_id>/addTs/', views_ventana.WindowOpenView.as_view(), name='window-add-ts'),
    path('room/<str:room_name>/window/<str:window_id>/activity/', views_ventana.get_recent_window_activity, name='window-activity'),
    path('room/<str:room_name>/light/all/', views_luz.get_all_lights, name='light-all'),
    path('room/<str:room_name>/light/create/', views_luz.LightView.as_view(), name='light-create'),
    path('room/<str:room_name>/light/<str:light_id>/', views_luz.LightView.as_view(), name='light')
]
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.RoomCreateView.as_view(), name='room'),
    path('home/', views.Home.as_view(), name='home')
]

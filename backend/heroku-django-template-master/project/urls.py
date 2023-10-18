from django.urls import path

from . import views
from .views import RoomCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('api/room/create', views.RoomCreateView.as_view(), name='room-create'),
    path('home/', views.Home.as_view(), name='home'),

]

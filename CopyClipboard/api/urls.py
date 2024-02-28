from django.urls import path
from .views import RoomView
from .views import UserView


urlpatterns = [
    path('room', RoomView.as_view()),
    path('user', UserView.as_view())
]
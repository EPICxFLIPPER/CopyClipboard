from django.urls import path
from .views import RoomView
from .views import UserView


urlpatterns = [
    path('home', RoomView.as_view()),
    path('user', UserView.as_view())
]
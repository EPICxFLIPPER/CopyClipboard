from django.urls import path
from .views import RoomView, UserView, CreateRoomView, CreateUserView

#Defines the url paths after /api:
urlpatterns = [
    path('room', RoomView.as_view()),
    path('user', UserView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('create-user', CreateUserView.as_view())

]
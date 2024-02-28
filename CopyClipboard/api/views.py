from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .serializers import UserSerializer
from .models import Room
from .models import User

# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
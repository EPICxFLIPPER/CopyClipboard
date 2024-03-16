from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .serializers import UserSerializer
from .models import Room
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

#Effects: Allows us to view a list of all rooms
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
#Effects: Allows us to view a list of all the users
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateRoomView(APIView):
   serializer_class = CreateRoomSerializer

   def post(self,request,format = None):
        if (not self.request.session.exists(self.request.session.session_key)):
           self.request.session.create()
        
        serializer = self.serializer_class(data = request.data)
        if (serializer.is_valid()):
            name = serializer.data.get('name')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host = host)
            if queryset.exists():
                room = queryset[0]
                room.name = name
                room.save(update_fields=['name'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host, name = name)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
        
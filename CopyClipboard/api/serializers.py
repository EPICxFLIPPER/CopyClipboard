##Translates modles into json response

from rest_framework import serializers
from .models import Room
from .models import User

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code','active_user','active_clipboard', 'created_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','user_name','password','in_room','clipboard', 'created_at')
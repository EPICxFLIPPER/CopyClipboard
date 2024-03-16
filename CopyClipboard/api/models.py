from django.db import models
import string
import random

#@param: length, the length of code to be generated, default to 8.
#Effects: Creates a unique code of upper case characters length length.
def generate_unique_code(length = 8):
    while (True):
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        if (Room.objects.filter(code =code).count() == 0):
            break
    return code


# Create your models here.
#Data structrue represents a Room a user can join to share their clipboards
#PRIMARY KEY code:             8 Character long uppercase code repreensting the room, eg AAAAAAAA
#            name:             the name of the room
#            active_user:      The username of the user whos clipboard is currently active in the room
#            active_clipboard: The contents that can be copied from this room by users
#            created _at:      The date and time this room was created at
class Room(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique = True, null = False)
    name = models.CharField(max_length = 20, default = "")
    host = models.CharField(max_length = 50, unique = True)
    active_user = models.CharField(max_length = 30, default = "", null = False)
    active_clipboard = models.TextField(max_length = 1000, default = "", null = False)
    created_at = models.DateTimeField(auto_now_add = True)


#Data structrue represents a User with an active clipbaord that can join rooms
#PRIMARY KEY user_name:   a users username, 30 characters long max, must be unique
#            password:    a users password
#FORIGN KEY  in_room:     the current room the user is in 
#            clipboard:   The contents that the user is sharing to other users
#            created _at: The date and time this user was created at
class User(models.Model):
    user_name = models.CharField(max_length = 30, null = False, unique = True)
    password = models.CharField(max_length = 30, null = False)
    host = models.CharField(max_length = 50, unique = True)
    in_room = models.CharField(max_length = 8, default = "")
    clipboard = models.TextField(max_length = 1000, default = "", null = False)
    created_at = models.DateTimeField(auto_now_add = True)



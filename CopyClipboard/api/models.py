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
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique = True, null = False)
    active_user = models.CharField(max_length = 30, default = "", null = False)
    active_clipboard = models.TextField(max_length = 1000, default = "", null = False)
    created_at = models.DateTimeField(auto_now_add = True)

class User(models.Model):
    user_name = models.CharField(max_length = 30, null = False, unique = True)
    password = models.CharField(max_length = 30, null = False)
    in_room = models.CharField(max_length = 8, default = "")
    clipboard = models.TextField(max_length = 1000, default = "", null = False)
    created_at = models.DateTimeField(auto_now_add = True)



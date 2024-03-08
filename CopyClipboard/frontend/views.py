from django.shortcuts import render

# Create your views here.

#Renders the frontend/html file
def index(request, *args, **kwargs):
    return render(request,'frontend/index.html')
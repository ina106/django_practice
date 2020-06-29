from django.shortcuts import render
from .models import Gall

# Create your views here.

def home(request):
    Gall_obj = Gall.objects
    return render(request,'home.html', {"home_key" : Gall_obj})

def create(request):
    return render(request, 'create.html')


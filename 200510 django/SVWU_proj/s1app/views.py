from django.shortcuts import render,get_object_or_404,redirect
from .models import Gall

# Create your views here.

def home(request):
    Gall_obj = Gall.objects
    return render(request,'home.html', {"home_key" : Gall_obj})

from django.shortcuts import render
from .models import Youtube

# Create your views here.

def home(request):
    youtube = Youtube.objects
    return render(request,'home.html',{'key':youtube})
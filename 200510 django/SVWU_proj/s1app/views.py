from django.shortcuts import render,get_object_or_404,redirect
from .models import Gall

# Create your views here.

def home(request):
    Gall_obj = Gall.objects
    return render(request,'home.html', {"home_key" : Gall_obj})

def detail(request,detail_id):
    detail_obj = get_object_or_404(Gall, pk=detail_id)
    return render(request,'detail.html',{"detail.key":detail_obj})

def create(request):
    if request.method == "POST":
        img_val=Gall()
        img_val.title=request.POST['titleImg']
        img_val.image=request.FILES['fileImg']
        img_val.date=request.POST['dateImg']
        img_val.summ=request.POST['summImg']
        img_val.save()
        return redirect('home')
    else:
        pass
    return render(request,'create.html')

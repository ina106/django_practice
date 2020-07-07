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

def edit(request,change_id):
    change_obj = get_object_or_404(Gall,pk=change_id)
    if request.method == "POST":
        change_obj.title = request.POST['titleImg']
        change_obj.img = request.FILES['fileImg']
        change_obj.date = request.POST['dateImg']
        change_obj.summ = request.POST['summImg']
        change_obj.save()
        return redirect(reverse('detail', args=(change_id,)))
    else:
        pass
    return render(request,'edit.html',{"edit_key":change_id})

def delete(request,delete_id):
    delete_obj = get_object_or_404(Gall, pk = delete_id)
    delete_obj.delete()
    return redirect('home')

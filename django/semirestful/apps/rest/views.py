from django.shortcuts import render,redirect
from .models import User

# Create your views here.

def index(request):
    print User.objects.all()
    context = {
        'users':User.objects.all()
    }
    return render(request,"rest/index.html",context)

def addpage(request):
    return render(request,"rest/add.html")

def adduser(request):
    if request.method == 'POST':
        fullname = request.POST['firstname'] + " " + request.POST['lastname']
        user = User.objects.create(name=fullname,email=request.POST['email'])
    return redirect('/')

def show(request,id):
    context = {
        "user": User.objects.get(id =id)
    }
    return render(request,"rest/show.html",context)
def deleteuser(request,id):
    User.objects.get(id = id).delete()
    return redirect('/')

def edit(request,id):
    context = {
        "user": User.objects.get(id =id)
    }
    return render(request,"rest/edit.html",context)

def edituser(request,id):
    if request.method == 'POST':
        user = User.objects.get(id = id)
        user.name = request.POST['firstname'] + " " + request.POST['lastname']
        user.email = request.POST['email']
        user.save()
    return redirect('/')
       
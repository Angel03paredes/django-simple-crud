from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import UserForm 
from crudusers.models import User


def index(request):
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html",{"message":"Angel"})

def userCreate(request):
    
    form = UserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create(name=name,email=email,password=password)
    
    return redirect("/")

def userUpdate(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        id=request.POST.get("id")

        User.objects.filter(pk=id).update(name=name,email=email,password=password)
    
    return redirect("/")

def userDelete(request,id):
    if request.method == 'GET':
         User.objects.filter(id=id).delete()

    return redirect("/")
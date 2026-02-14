from django.shortcuts import render, redirect
from .models import User
from . import models

# Create your views here.

def index(request):
    context = {
        'all_users' : models.get_all_users() 
    }
    return render(request, 'index.html', context)

def submit_user(request):
    if request.method == 'POST':
        models.create_user(request.POST)
        print(models.create_user(request.POST))

    return redirect('/')

def delete_by_id(request):
    if request.method == 'POST': 
        user_id = request.POST['user_id']
    models.delete_user(user_id)

    return redirect('/')

def remove_user_by_id(request):
    if request.method =='POST':
        id = request.POST['user_to_delete']
        models.remove_user_by_id(id)
        
    return redirect('/')
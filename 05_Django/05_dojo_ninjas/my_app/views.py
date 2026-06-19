from django.shortcuts import render, redirect
from . import models

# Create your views here.

def index(request):
    #get dojos and ninjas
    context = {
        'all_dojos': models.get_dojos(),
        'all_ninjas' : models.get_ninjas()
    }
    return render(request, 'index.html', context)


def add_dojo(request):
    if request.method == 'POST':
        models.create_dojo(request.POST)
        print('DOJO CREATED SUCCESSFULLY')
    return redirect('/')

def add_ninja(request):
    if request.method == 'POST':
        models.create_ninja(request.POST)
        print('NINJA CREATED SUCCESSFULLY')
    return redirect('/')

def delete_dojo(request):
    if request.method == 'POST':
        models.delete_dojo(request.POST)
        print('DOJO DELETED SUCCESSFULLY')
    return redirect('/')
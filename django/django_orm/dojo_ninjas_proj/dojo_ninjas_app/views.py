from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    request.session['counter'] = 0
    context = { 
        'alldojos' : models.get_dojos(),
        'allninjas': models.get_ninjas(),
    }
    return render(request, 'index.html', context) #get all dojos


def register_dojo(request):
    if request.method == 'POST':
        models.create_dojo(request.POST)

    return redirect('/')


def register_ninja(request):
    if request.method == "POST":
        models.create_ninja(request.POST)

    return redirect('/')


def delete_dojo_id(request):
    if request.method == 'POST':
        dojo_id = request.POST['dojo_id']
        models.delete_dojo(dojo_id)

    return redirect('/')

    


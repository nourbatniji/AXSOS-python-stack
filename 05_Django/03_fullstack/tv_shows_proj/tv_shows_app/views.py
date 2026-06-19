from django.shortcuts import render, redirect
from . import models
from .models import Show
from django.contrib import messages
# Create your views here.


def index(request):
    return redirect('/shows')


def display_all(request):
    context = {
        'shows' : models.display_all()
    }
    return render(request, "index.html",context)


def add_show_page(request):
    return render(request, 'add_show.html')


def add_show(request):

   if request.method == 'POST':
        errors = Show.objects.validate_show(request.POST) 

        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val)
            return render(request, 'add_show.html') ##### Why the redirect didn't work, as the material it should be redirect but it didn't work
        
        else:
            show = models.create_show(request.POST)
            return redirect(f'/shows/{show.id}')


def show_details(request, id):
    context = {
        'show' : models.show_details(id)
    }

    return render(request, 'view_show.html', context)


def update_page(request, id):
    context = {
        'show' : models.show_to_update(id)
    }
    return render(request, 'update_show.html', context)


def edit_show(request, id):
    if request.method == 'POST':
        errors = Show.objects.validate_show(request.POST)
        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val)
            return redirect(f'/shows/{id}/edit')
        
        else:
            models.edit_show(request.POST, id)
            return redirect(f'/shows/{id}/edit')


def delete_show(request,id):
    models.delete_show_by_id(request,id)
    return redirect('/shows')
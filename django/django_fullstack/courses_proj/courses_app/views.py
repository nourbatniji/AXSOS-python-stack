from django.shortcuts import render, redirect
from . import models
from django.views.decorators.csrf import csrf_exempt # Use only if necessary, prefer CSRF token in client-side


# Create your views here.
def index(request):
    context = {
        'courses' : models.display_courses()
    }
    return render(request, 'index.html', context)

def add_course(request):
    if request.method == 'POST':
        models.create_course(request.POST)

    return redirect('/')


def delete_course_page(request, id):
    context = {
        'course' : models.delete_page(id)
    }
    return render(request, 'delete.html', context)


def delete_course(request, id):
    models.delete_course(id)
    return redirect('/')

def comments_page(request, id): ##renders comments page
    context = {
        'course_id' : id,
        'comments' : models.display_comments(id)
    }
    return render(request, 'comments.html', context)


def add_comment(request, id): ## creates comment
    if request.method == 'POST':
        models.add_comment(request.POST, id)
    print("adddeeedd successfully")
    return redirect(f'/courses/comment/{id}') #display comments


def delete_comment(request, id):

    models.delete_comment(request.POST['comment_id'])
    return redirect(f'/courses/comment/{id}')
from django.shortcuts import render, redirect
from . import models


# Create your views here.

def index(request):
    context ={
        'allbooks' : models.show_books()
    }
    
    return render(request, 'index.html', context)


def add_book(request):
    if request.method == 'POST':
        models.addBook(request.POST)

    return redirect('/')
    

def books(request, id):
    context = {
        'details' : models.book_details(id)
    }
    return render(request, 'bookDetails.html', context)


def add_author_to_book(request):
    if request.method =='POST':
        book_id = request.POST['book_id']
        author_id = request.POST['author_id']
        models.add_author_to_book(book_id, author_id)

    return redirect(f'/books/{book_id}')

def delete_book_by_id(request):
    if request.method == 'POST':
        models.delete_book(request.POST)
    return redirect('/')
    
    

##########################

def authors_page(request):
    context = {
        'authors' : models.show_authors()
    }
    return render(request, 'authors.html', context)

def add_author(request):
    if request.method == 'POST':
        models.add_author(request.POST)
        print(request.POST)
    return redirect('/authors')


def authors(request, id):
    context = {
        'details' :models.author_details(id)
    }
    return render(request, 'author_details.html', context)
    

def add_book_to_author(request):
    if request.method == 'POST':
        author_id = request.POST['author_id']
        book_id = request.POST['book_id']

        models.add_book_to_author(author_id, book_id)
    return redirect(f'authors/{author_id}')


def delete_author_by_id(request):
    if request.method == 'POST':
        author_id = request.POST['author_id']
        models.delete_author(author_id)
        print(author_id)

    return redirect('/authors')
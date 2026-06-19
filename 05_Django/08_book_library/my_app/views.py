from django.shortcuts import render, redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt


# LANDING PAGE
def index(request):
    request.session['is_logged'] = False
    return render(request, 'index.html')

#============================================================
# SIGN UP
def reg_user(request):
    if request.method == 'POST':
        errors = User.objects.validate_reg(request.POST)
        user = User.objects.filter(email=request.POST['email'])
        
        #check if errors
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False
            return redirect('/')

        #check if email already exists
        if user:
            messages.error(request, 'Email already exists!')
            request.session['is_logged'] = False
            return redirect('/')

        #if pass validation, register
        else:
            user_created = models.create_user(request.POST)
            request.session['user_id'] = user_created.id
            request.session['is_logged'] = True
            return redirect('/books')
    
    return redirect('/')

#============================================================
# SIGN IN
def login_user(request):
    if request.method == 'POST':
        errors = User.objects.validate_login(request.POST)
        user = User.objects.filter(email=request.POST['email'])
        #if validation errors
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False
            return redirect('/')
        #check if email exists
        if user:
            logged_user = user[0]
            #check pass 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['is_logged'] = True
                request.session['user_id'] = logged_user.id
                return redirect('/books')
            #wrong pass
            else: 
                messages.error(request, 'Incorrect password')
                request.session['is_logged'] = False
                return redirect('/')
        #emial doesn't exist
        else:
            messages.error(request, 'User does not exist')
            request.session['is_logged'] = False
            return redirect('/')
        

#============================================================
# HOME PAGE
def books(request):
    if not request.session.get('is_logged'):
        return render(request, 'index.html')
    
    context ={ 
        'user' : models.get_user_by_id(request.session.get('user_id')),
        'all_books' : models.get_all_books(),
        'liked_books' : models.get_user_likes(request.session.get('user_id'))
    }
    return render(request, 'books.html', context)

#============================================================
# REGISTER A BOOK AND ADD IT TO FAVORITES
def add_fav_book(request):
    if not request.session.get('is_logged'):
        return render(request, 'index.html')
    if request.method == 'POST':
        models.add_fav_book(request.POST)
        return redirect('/books')

#============================================================
# BOOK DETAILS PAGE
def book_details(request, id):
    if not request.session.get('is_logged'):
        return render(request, 'index.html')
    
    context = {
        'book' : models.get_book_by_id(id),
        'user' : models.get_user_by_id(request.session.get('user_id')),
        'liked_books' : models.get_user_likes(request.session.get('user_id'))
    }
    return render(request, 'book.html', context)

#============================================================
# UPDATE
def update_book(request):
    if not request.session.get('is_logged'):
        return render(request, 'index.html')
    if request.method == 'POST':
        models.update_book(request.POST)
        print('UPDATED SUCCESSFULLY')
        return redirect('/books')
    
#============================================================
# DELETE BOOK FROM DB
def delete_book(request):
    if not request.session.get('is_logged'):
        return render(request, 'index.html')
    if request.method == 'POST':
        models.delete_book(request.POST)
        print('DELETED SUCCESSFULLY')
        return redirect('/books')
    
    
#============================================================
# ADD BOOK TO FAVORITES
def add_book_to_user_likes(request):
    if not request.session.get('is_logged'):
        return render(request, 'index.html')
    if request.method == 'POST':
        models.add_book_to_fav(request.POST)
        print('ADDEDD SUCCESSFULLY')
        return redirect('/books')

#============================================================
# REMOVE BOOK TO FAVORITES
def delete_book_from_fav(request):
    if not request.session.get('is_logged'):
        return render(request, 'index.html')
    if request.method == 'POST':
        models.del_from_fav(request.POST)
        print('DELETED SUCCESSFULLY')
        return redirect('/books')
    
#============================================================
def logout(request):
    del request.session['is_logged']
    return redirect('/')

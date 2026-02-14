from django.shortcuts import render, redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    request.session['is_logged'] = False
    return render(request, 'index.html')



#----------------------------------------------------------
#VALIDATIONS / LOGIN / REGISTER / LOGOUT
def register_user(request):
    if request.method == 'POST':
        errors = User.objects.reg_valid(request.POST)
        user_email = User.objects.filter(email = request.POST['email'])
        #check validation errors
        if len(errors)>0:
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False
            return redirect('/')
        
        #check unique email
        # if user_email:
        #     messages.error(request, "User already exists")
        #     request.session['is_logged'] = False
        #     return redirect('/')
        
        #if passed validation and email is unique
        else:
            user = models.create_user(request.POST)
            request.session['user_id'] = user.id
            print("USER CREATED SUCCESSFULLY")
            request.session['is_logged'] = True
            return redirect('/books_home')
    return redirect('/')


def login_user(request):
    if request.method == 'POST':
        errors = User.objects.valid_login(request.POST)
        user = User.objects.filter(email = request.POST['email'])
        #check validation errors
        # if len(errors)>0:
        #     for key, val in errors.items():
        #         messages.error(request, val)
        #     request.session['is_logged'] = False
        #     return redirect('/')
        #if email exists
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                print("USER LOGGED IN SUCCESSFULLY")
                request.session['is_logged'] = True
                return redirect('/books_home')
            
            else:
                messages.error(request, "Incorrect Password")
                request.session['is_logged'] = False
                return redirect('/')
            
        else:
            messages.error(request, "User does not exist")
            request.session['is_logged'] = False
            return redirect('/')
        
    return redirect('/')



def logout_user(request):
    del request.session['is_logged']
    print("USER is OUT SUCCESSFULLY")
    return render(request, 'index.html')


#----------------------------------------------------------
#BOOKS PAGE / HOME PAGE

def books_home(request):
    if not request.session.get('is_logged'):
        return redirect('/')
    
    context = {
        'logged_user' : models.get_user_byid(request.session.get('user_id')),
        'books' : models.get_all_books()
    }
    return render(request, 'books_home.html', context)



def add_book_page(request):
    if not request.session.get('is_logged'):
        return redirect('/')
    
    context = {
        'logged_user' : models.get_user_byid(request.session.get('user_id'))    }
    
    return render(request, 'add_book.html', context)

def add_book(request):
    if not request.session.get('is_logged'):
        return redirect('/')
    
    print("BOOK CREATED SUCCESSFULLY")

    models.create_book(request.POST)
    return redirect('/books_home')


def book_details(request, id):
    if not request.session.get('is_logged'):
        return redirect('/')
    context = {
        'book' : models.get_book_byid(id)
    }
    
    return render(request, 'book.html', context)
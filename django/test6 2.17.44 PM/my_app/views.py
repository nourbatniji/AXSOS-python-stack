from django.shortcuts import render, redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    request.session['is_logged'] = False
    return render(request, 'index.html')

#_______________________________________________________
# REGISTER
def create_user(request):
    if request.method == 'POST':
        errors = User.objects.reg_validator(request.POST)
        
        #check if errors
        if len(errors) > 0:
            context ={
                'errors' : errors
            }
            request.session['is_logged'] = False
            return render(request, 'index.html', context)

        else:
            user_created = models.create_user(request.POST)
            request.session['is_logged'] = True
            request.session['user_id'] = user_created.id
            print("USER CREATED ")
            return redirect('/books')
    
#_______________________________________________________      
# LOGIN
def login_user(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        user = User.objects.filter(email=request.POST['email'])
        #if validation errors
        if len(errors) > 0:
            context ={
                'login_errors' : errors
            }
            request.session['is_logged'] = False
            return render(request, 'index.html', context)
        #check if email exists

        logged_user = user[0]
        #check pass 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['is_logged'] = True
            request.session['user_id'] = logged_user.id
            print("LOGGEDIN SUCCESSFULLY")
            return redirect('/books')
            #wrong pass
        else: 
            errors['pass_not_correct'] = 'Incorrect password'
            request.session['is_logged'] = False
            print("LOGGEDIN NNOOOOOOO")
            return redirect('/')
       

    
#_______________________________________________________      
# HOME PAGE
def books_page(request):
    if 'is_logged' not in request.session:
        return render(request, 'index.html')
    context = {
        'logged_user_id' : request.session.get('user_id'), 
    }
    return render(request, 'books_home.html', context)
     





#_______________________________________________________      
# LOGOUT
def logout(request):
    del request.session['is_logged']

    return render(request, 'index.html')
from django.shortcuts import render, redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    request.session['is_logged'] = True
    return render(request, 'index.html')


def signup_page(request):
    return render(request, 'signup.html')

def signin_page(request):
    return render(request, 'login.html')


def sign_up(request): #creates user
    if request.method == "POST":
        errors = User.objects.reg_validation(request.POST)
        email = User.objects.filter(email = request.POST['email'])
        if email:
            messages.error(request, 'Email already exists')
            request.session['is_logged'] = False
            return redirect('/register')
        if errors:
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False
            return redirect('/register')
        else:
            models.create_user(request.POST)
            request.session['is_logged'] = True
            print('created successfully')
            return redirect('/')
            
    return redirect('/register')



def sign_in(request):
    if request.method == "POST": #if post
        errors = User.objects.login_validation(request.POST) 
        user = User.objects.filter(email = request.POST['email'])

        if len(errors) > 0: #check if errors
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False
            return redirect('/signin')

        else: #if no errors
            if user: #user exist?
                logged_user = user[0]
                #pass match?
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    print('matched')
                    request.session['is_logged'] = True
                    return redirect('/dashboard')
                #no match?
                else:
                    print("incorrect")
                    messages.error(request, 'Incorrect Password')
                    request.session['is_logged'] = False
                    return redirect('/signin')
            #no user?
            else:
                messages.error(request, 'User does not exist')
                request.session['is_logged'] = False
        return redirect('/signin')



def display_all_users(request):
    context = {
        'all_users' : models.display_all_users()
    }
    return render(request, 'user_dash.html', context)






def new_user_page(request):
    return render(request, 'new_user.html')


        
        
        

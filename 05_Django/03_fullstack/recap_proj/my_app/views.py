from django.shortcuts import render, redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    request.session['is_logged'] = False
    return render(request, 'index.html')


def signup_page(request):
    request.session['is_logged'] = False
    return render(request, 'signup.html')


def sign_up(request):
    if request.method == "POST":
        errors = User.objects.reg_validation(request.POST)
        user = User.objects.filter(email = request.POST['email'])
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False
            return redirect('/go_to_signup')
        
        elif user:
            messages.error(request, "Email already exists!")
            request.session['is_logged'] = False
            return redirect('/go_to_signup')
        
        else:
            models.create_user(request.POST)
            request.session['is_logged'] = True
            return redirect('/homepage')
    
    return redirect("/")


def login_page(request):
    request.session['is_logged'] = False
    return render(request, 'login.html')


def log_in(request):
    if request.method == "POST":
        errors = User.objects.login_validation(request.POST)
        user = User.objects.filter(email = request.POST['email'])
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False
            return redirect('/go_to_login')
    
        #check if user exists
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['is_logged'] = True
                return redirect('/homepage')
            
            else:
                messages.error(request, "Incorrect password")
                request.session['is_logged'] = False
                return redirect('/go_to_login')
            
        else:
            messages.error(request, 'User does not exist')
            request.session['is_logged'] = False
            return redirect('/go_to_login')
    return redirect('/')



def home_page(request):
    is_logged = request.session.get('is_logged')
    if is_logged:
        return render(request, 'home.html')
    else:
        return render(request, 'index.html')
    

def users_page(request):
    context = {
        'users' : models.display_all_users()
    }
    is_logged = request.session.get('is_logged')
    if is_logged:
        return render(request, 'allUsers.html', context)
    else:
        return render(request, 'index.html')


def user_details(request, id):
    context = {
        'userdetails' : models.get_by_id(id)
    }
    is_logged = request.session.get('is_logged')
    if is_logged:
        return render(request, 'user_details.html', context)
    else:
        return render(request, 'index.html')


def sign_out(request):
    del request.session['is_logged']
    return render(request, 'login.html')


def delete_user(request):
    if request.method == 'POST':
        models.delete_user(request.POST['user_id'])
    return redirect('/users')


def update_page(request, id):
    context = {
        'userdetails' : models.get_by_id(id)
    }
    is_logged = request.session.get('is_logged')
    if is_logged:
        return render(request, 'update.html', context)
    else:
        return render(request, 'index.html')

def edit_user(request, id):
    if request.method == 'POST':
        models.edit_user(request.POST, id)
    return redirect('/users')



def address_page(request, id):
    context = {
        'user': id
    }

    is_logged = request.session.get('is_logged')
    if is_logged:
        return render(request, 'add_address.html', context)
    else:
        return render(request, 'index.html')



def add_address(request):
    if request.method == 'POST':
        models.add_new_address(request.POST)
        return redirect('/users')



def user_addresses_page(request, id):
    context = {
        'address' : models.get_user_address(id)
    }
    return render(request, 'addres_user.html', context)





            

from django.shortcuts import render, redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt


# Create your views here.

def index(request):
    request.session['is_logged'] = False
    return render(request, 'index.html')

def success(request, id):
    context = {
        'user' : models.get_user_by_id(id)
    }
    logged = request.session.get('is_logged')
    if logged == True:
        return render(request, 'success.html', context)
    else:
        return redirect('/')


def reg_user(request):
    if request.method == "POST":
        errors = User.objects.validate_reg(request.POST)
        user_email = User.objects.filter(email=request.POST['email'])
        #check validation
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False    
            return redirect("/")
        
        #if email unique
        elif user_email:
            messages.error(request, 'Email already exists')
            request.session['is_logged'] = False    
            return redirect("/")

        #no errors? signup
        else:
            user = models.create_user(request.POST)
            request.session['is_logged'] = True
            return redirect(f'/success/{user.id}')
    else:
        return redirect("/")
    

def login_user(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        user = User.objects.filter(email = request.POST['email'])

        #check validation
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            request.session['is_logged'] = False
            return redirect('/')
        
        #if no errors:
        else:
            #if user exisits
            if user:
                logged_user= user[0]
                #check entered pw with already hashed pw
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['is_logged'] = True
                    return redirect(f'/success/{logged_user.id}')
                #if not matched with the stored
                else:
                    request.session['is_logged'] = False
                    messages.error(request, "Incorrect password!")
                    return redirect("/")
            #if user does not exist
            else:
                request.session['is_logged'] = False
                messages.error(request, 'User does not exist')
        return redirect("/")

def log_out(request):
    del request.session['is_logged']
    return redirect("/")
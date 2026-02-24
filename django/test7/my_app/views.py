from django.shortcuts import render, redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    request.session['is_logged'] = False
    return render(request, 'index.html')

# --------------------------------------------------

#VALIDATION / REGISTER / LOGIN / LOGUT 
def create_user(request):
    if request.method == 'POST':
        errors = User.objects.validate_reg(request.POST)
        if len(errors) > 0: 
            context = {
                'errors' : errors
            }
            print(context['errors'])
            request.session['is_logged'] = False
            return render(request, 'index.html', context)
        
        else: 
            user = models.create_user(request.POST)
            request.session['user'] = user.id
            request.session['is_logged'] = True
            return redirect('/books')
    return redirect('/')

# --------------------------------------------------

def login_user(request):
    if request.method == 'POST':
        errors = User.objects.validate_login(request.POST)
        user = models.get_email(request.POST['email'])  #user email

        #check validation errors
        if len(errors) > 0: 
            context = {
                'errors' : errors
            }
            request.session['is_logged'] = False
            return render(request, 'index.html', context)
        
        #if user email exisits
        if user:
            print("EMAIL FOUND ")
            #check pass 
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user'] = logged_user.id
                request.session['is_logged'] = True
                return redirect('/books')
            #if not matched
            else:
                errors['wrong_pass'] = 'Incorrect password'
                context = {
                    'errors' : errors
                }
                request.session['is_logged'] = False
                return render(request, 'index.html', context)

# --------------------------------------------------

def logout(request):
    request.session.flush()
    return render(request, 'index.html')


# --------------------------------------------------
# --------------------------------------------------




def books_page(request):
    if 'is_logged' not in request.session:
        return render(request, 'index.html')
    
    context = {
        'logged_user' : models.get_id(request.session.get('user')),
        'reviews' : models.get_all_reviews()
    }
    
    return render(request, 'books_home.html', context)




def add_book_pg(request):
    if 'is_logged' not in request.session:
        return render(request, 'index.html')
    
    context = {
        'logged_user' : models.get_id(request.session.get('user'))
    }
    
    return render(request, 'add_book.html', context)



def create_book(request):
    if 'is_logged' not in request.session:
        return render(request, 'index.html')
    
    if request.method == 'POST':
        models.create_book(request.POST)
        print("BOOK CREATED SUCCESSFULLT")
        return redirect('/books')

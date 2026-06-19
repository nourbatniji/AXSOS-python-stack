from django.shortcuts import render, redirect
from . import models
from .models import User, Tree
import bcrypt

# Create your views here.


def index(request):
    request.session['is_logged'] = False
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST': 
        errors = User.objects.validate_signup(request.POST)
        if errors:
            request.session['is_logged'] = False
            print('errors signup')
            return render(request, 'index.html', {'errors': errors})
        else:
            user = models.create_user(request.POST)
            request.session['is_logged'] = True
            request.session['user_id'] = user.id
            print('signup done')
            return redirect('/dashboard')
        

def login(request):
    if request.method == 'POST': 
        login_errors = User.objects.validate_login(request.POST)
        user = User.objects.filter(email=request.POST['login_email'])
        if login_errors:
            request.session['is_logged'] = False
            print('errors login')
            return render(request, 'index.html', {'login_errors': login_errors})
        else:
            if user:
                logged_user = user[0]
                if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.passwrod.encode()):
                    request.session['is_logged'] = True
                    request.session['user_id'] = logged_user.id
                    print('logged')
                    return redirect('/dashboard')
                else:
                    login_errors['incorrect_pw'] = "Incorrect password"
                    print('incorrect')
                    return render(request, 'index.html', {'login_errors': login_errors})
    return render(request, 'index.html')


def sign_out(request):
    request.session.flush()
    return redirect('/')

def dashboard(request):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'trees' : models.get_all_trees()
    }
    return render(request, 'dashboard.html', context)





def add_tree_page(request):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'tree.html', context)







def create_tree(request):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    if request.method == 'POST':
        errors = Tree.objects.validate_tree(request.POST)
        context = {
            'user' : User.objects.get(id=request.session['user_id']), 
            'errors':errors
        }
        if errors:
            return render(request, 'tree.html', context)
        
        else:
            models.create_tree(request.POST)
            return redirect('/dashboard')
    

def delete_tree(request):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    if request.method == 'POST':
        models.delete_tree(request.POST)
        return redirect('/dashboard')
    


def tree_details_page(request, id):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    has_visited = False
    
    context = {
        'logged_user' : User.objects.get(id=request.session['user_id']),
        'tree' : models.get_tree_by_id(id), 
        'visits' : models.get_visits(id), 
        'has_visited':has_visited
    }

    return render(request, 'tree_details.html', context)

has_visited = False

def visit_tree(request, id):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    has_visited = False
    
    if request.method == 'POST':
        models.visit_tree(request.POST, id)
        has_visited = True

    context = {
        'logged_user' : User.objects.get(id=request.session['user_id']),
        'tree' : models.get_tree_by_id(id), 
        'visits' : models.get_visits(id), 
        'has_visited' : has_visited
    }
        
    return render(request, 'tree_details.html', context)



def edit_tree_page(request, id):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'tree' : models.get_tree_by_id(id)
    }
    return render(request, 'update.html', context)



def edit_tree(request, id):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    if request.method == 'POST':
        errors = Tree.objects.validate_tree(request.POST)
        context = {
            'user' : User.objects.get(id=request.session['user_id']),
            'tree' : models.get_tree_by_id(id),
            'errors':errors
        }
        if errors:
            return render(request, 'update.html', context)
        
        else:
            models.update_tree(request.POST)
            return redirect('/dashboard')
    
    return render(request, 'update.html')




def zipcode_page(request, id):
    if 'is_logged' not in request.session:
        return render(request, 'not_found.html')
    
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'zip' : models.get_zip_by_id(id)
    }
    return render(request, 'zipcode.html', context)


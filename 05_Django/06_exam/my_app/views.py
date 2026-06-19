from django.shortcuts import render, redirect
from . import models 
from .models import User, Game
import bcrypt

# Create your views here.

def index(request):
    request.session['is_logged'] = False
    return render(request, 'index.html')



# VALIDATIONS
#----------------------------------------
# REGISTRATION
def register(request):
    if request.method == 'POST':
        errors = User.objects.reg_validation(request.POST)
        if len(errors) > 0:
            context = {
                'errors' : errors
            }
            request.session['is_logged'] = False
            return render(request, 'index.html', context)
         
        else:
            user = models.create_user(request.POST, request.FILES)
            request.session['user'] = user.id
            request.session['is_logged'] = True
            return redirect('/dashboard')      

#----------------------------------------
# LOGIN
def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)
        user_email = models.get_email(request.POST['email'])

        #check validation errors
        if len(errors) > 0:
            context = {
                'errors' : errors
            }
            request.session['is_logged'] = False
            return render(request, 'index.html', context)
        
        if user_email:
            logged_user = user_email[0]
            #if correct pass
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user'] = logged_user.id
                request.session['is_logged'] = True
                return redirect('/dashboard')      
            
            #if incorrect pass
            else:
                errors['incorrect_pass'] = "Incorrect password"
                context = {
                'errors' : errors
                }
                request.session['is_logged'] = False
                return render(request, 'index.html', context)
            
    return redirect('/')   
            

#----------------------------------------
# LOG OUT
def logout(request):
    request.session.flush()
    print("LOGGED OUT")
    return render(request, 'index.html')


#-------------------------------------------------------------------------------

def dashboard(request):
    if 'is_logged' not in request.session:
        return render(request, 'index.html')
    
    context = {
        'user' : models.get_user_by_id(request.session.get('user')),
        'all_games' : models.get_all_games()
    }
    return render(request, 'dashboard.html', context)



def add_game(request):
    if request.method == 'POST':
        errors = Game.objects.game_validation(request.POST)
        if len(errors) > 0:

            context = {
                'errors' : errors
            }

            return render(request, 'dashboard.html', context)
        
        else:
            models.create_game(request.POST)
            print('GAME CREATED SUCCESSFULLY')
            return redirect('/dashboard')
        


def got_to_game(request, id):
    context = {
        'user' : models.get_user_by_id(request.session.get('user')),
        'game' : models.get_game_by_id(id), 
        'fans' : models.get_games_fans(id)
    }

    return render(request, 'game_details.html', context)



def go_to_edit(request, id):
    context = {
        'user' : models.get_user_by_id(request.session.get('user')),
        'game' : models.get_game_by_id(id)
    }
    return render(request, 'update_game.html', context)


def update_game(request, id):
     if request.method == 'POST':
        errors = Game.objects.game_validation(request.POST)
        if len(errors) > 0:
            context = {
                'errors' : errors
            }
            return render(request, 'update_game.html', context)
        
        else:
            models.update_game(request.POST, id)
            return redirect('/dashboard')
        


def delete_game(request):
    if request.method == 'POST':
        models.delete_game(request.POST)

    return redirect('/dashboard')

    


def order_games(request):

    context = {
        'user' : models.get_user_by_id(request.session.get('user')),
        'all_games' : models.order_games()
    }
    return render(request, 'dashboard.html', context)



def add_game_to_favorite(request):
    if request.method == 'POST':
        models.add_game_to_favorite(request.POST)
        return render(request, 'game_details.html')



    

    

def gamer_details(request, id):
    context = {
        'user' : models.get_user_by_id(id),
        'games' : models.get_user_favorites(id)

    }
    return render(request, 'gamer_details.html', context)
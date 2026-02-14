from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    request.session['random_number'] = random.randint(1, 100)
    print(f'random: {request.session["random_number"]}')
    return render(request,"index.html")


def guess_number(request):
    request.session['user_guess'] = request.POST['number']
    random_number = request.session['random_number']
    user_guess = int(request.session['user_guess'])
    
    if 'counter' not in request.session:
        request.session['counter'] = 0

    if user_guess>100 or user_guess<1:
        message = "Please choose a number between 1 and 100"

    else:
        request.session['counter'] += 1
        if user_guess>random_number:
            message = "Too High!"

        elif user_guess<random_number:
            message = "Too Low!"

        elif user_guess == random_number:
            message = f"Congrats, {user_guess} was the number!🥳"
            
        
    if request.session['counter'] >= 5:
        message = f"You Lose!😭"

    context = {
        'message' : message,
        'attempts' : request.session['counter']
    }
    return render(request,"index.html", context)



def play_again(request):
    request.session['counter'] = 0
    print(request.session['counter'] )
    return redirect('/')


def winners(request):
    request.session['winner'] = request.POST['username']
    winner = request.session['winner']
    if ("winners_list" not in request.session):
        request.session['winners_list'] = []
        
    request.session['winners_list'].insert(0, {'winner_name': winner, 'total_time': request.session['counter'] })


    winners_list = request.session['winners_list']

    context = {
        'winners' : winners_list, 
        'counter' : request.session['counter'] 
    }
    return render(request, 'show.html', context)


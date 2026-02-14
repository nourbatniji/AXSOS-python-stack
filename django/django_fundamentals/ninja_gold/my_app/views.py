from django.shortcuts import render, redirect
import random
from django.utils import timezone

# Create your views here.


def index(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return render(request, 'index.html')


def process_money(request, value):
    now = timezone.localtime(timezone.now())
    formatted_time = now.strftime("%Y/%m/%d %I:%M %p")
    counter = len(request.session['activities']) + 1

    if value=='farm':
        gold = random.randint(10, 20)
        message = f'You entered a {value} and earned {gold}. ({formatted_time})'
        
    elif value=='cave':
        gold = random.randint(5, 10)
        message = f'You entered a {value} and earned {gold}. ({formatted_time})'

    elif value=='house':
        gold = random.randint(2, 5)
        message = f'You entered a {value} and earned {gold}. ({formatted_time})'

    elif value=='quest':
        gold = random.randint(-50, 50)
        if gold>0:
            message = f'You entered a {value} and earned {gold}. ({formatted_time})'
            print(f'{gold}pos')
        if gold<0:
            message = f'You failed a {value} and lost {-gold}. Ouch. ({formatted_time})'
            print(f'{gold}neg')

    
    request.session['gold'] += gold
    request.session['activities'].insert(0, message)
    print(f"golds: { request.session['gold'] }")
    print(f"golds: { request.session['activities'] }")
    context = { 
        'message' : request.session['activities'],
        'gold' : request.session['gold']
        }
    if (counter <= int(request.session['moves']) and request.session['gold']>= int(request.session['golds'] )):
        context={
            'Message' :'Congrats, You Won!'
        }
    return render(request, 'index.html', context)
    
    
def reset_game(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')


def game_conditions(request):
    request.session['golds'] = request.POST.get('golds')
    request.session['moves'] = request.POST.get('moves')
    print(f'gold: {request.session["golds"]}')
    print(f'moves: {request.session["moves"]}')
    return redirect('/')
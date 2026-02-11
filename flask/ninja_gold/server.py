from flask import Flask, render_template, request, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'SECRET'

@app.route('/')
def index():
    session['gold'] = 0
    session['activity'] = []
    return render_template('index.html', gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def submit_form():
    value = request.form['building']
    now = datetime.now()
    formatted_time = now.strftime("%Y/%m/%d %I:%M %p")
    counter = len(session['activity'])

    if value == 'farm':
        gold = random.randint(10, 20)
        session['gold'] += gold
        message = f"Earned {gold} golds from the farm! ({formatted_time})"
        
    elif value == 'cave':
        gold = random.randint(5, 10)
        session['gold'] += gold
        message = f"Earned {gold} golds from the cave! ({formatted_time})"

    elif value == 'house':
        gold = random.randint(2, 5)
        session['gold'] += gold
        message = f"Earned {gold} golds from the house! ({formatted_time})"

    elif value == 'casino':
        gold = random.randint(-50, 50)
        if (gold>0):
            session['gold'] += gold
            message = f"Earned {gold} golds from the casino! ({formatted_time})"

        elif (gold<0): 
            session['gold'] += gold
            message = f"Earned a casino and lost {-gold} golds... Ouch.. ({formatted_time})"


    if (counter < 15 and  session['gold'] >= 100):
            Message = "Congrats, You Won!"
            return render_template('index.html', Message=Message)
    
    session['activity'].insert(0,message)
    
    return render_template('index.html', gold=session['gold'], message=session['activity'])


@app.route('/', methods=['POST'])
def reset_game():
    session['gold'] = 0
    session['activity'] = []
    session['counter'] = 0
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
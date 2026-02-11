from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'SECRET'


@app.route('/')
def index():
    # session['number'] = number
    random_num = random.randint(1, 100)
    session['random_int'] = random_num
    print(session['random_int'])
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def guess():
    session['entered_number'] = request.form['entered_number']
    user_number = int(session['entered_number'])
    random_num =session['random_int']



    if 'counter' not in session:
        session['counter'] = 0


    if (user_number > 100 or user_number < 1 or user_number == ''):
        answer = "Please choose a number between 1 to 100"
        session['counter'] += 1

    elif user_number < random_num:
        answer = "Too Low!"
        session['counter'] += 1

    elif user_number > random_num:
        answer = "Too High!"
        session['counter'] += 1

    elif user_number == random_num:
        answer = f"{user_number} Was the number! 🥳"
        session['counter'] = 0
    
    if session['counter'] == 5:
        session['counter'] = 0
        answer = 'You Lose! 😭'
    
    return render_template('index.html', answer=answer, counter = session['counter'])

@app.route('/startover', methods=['POST'])
def startover():
    session['counter'] = 0
    return redirect('/')


@app.route('/submit_winner', methods=['POST'])
def submit_winner():
    session['winner'] = request.form['winner_name']
    winner = session['winner']
    if ('winners_list' not in session):
        session['winners_list'] = []
    session['winners_list'].insert(0, {'winner_name': winner, 'total_times':session['counter']})
    winners_list = session['winners_list']

    return render_template('show.html', winners= winners_list)

if __name__ == "__main__":
    app.run(debug=True)
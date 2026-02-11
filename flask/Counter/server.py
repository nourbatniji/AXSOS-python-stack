from flask import Flask, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = "keep it secret"

@app.route('/')
def index():
    session['counter'] = 0
    if 'key_name' in session:
        session['key_name'] += 1
    else:
        session['key_name'] = 1
    return render_template('index.html',  visitingsCounter=session['key_name'])


@app.route('/takenum', methods=['POST'])
def start():
    counterByNum = request.form['counterByNum']
    session['counterByNum'] = counterByNum
    if 'key_name' in session:
        session['key_name'] += 1
    else:
        session['key_name'] = 1
    return render_template('index.html', counterByNum = counterByNum, visitingsCounter=session['key_name'])


@app.route('/increment', methods=['POST'])
def increment():
    session['counter']  += int(session['counterByNum'] )
    print(session['counter'] )
    if 'key_name' in session:
        session['key_name'] 
    else:
        session['key_name'] = 1
    return render_template('index.html', counter = session['counter'], visitingsCounter=session['key_name'])


@app.route('/counterBy2')
def counter2():
    if 'key_name' in session:
        session['key_name'] += 2
    else:
        session['key_name'] = 0
    return render_template("counterBy2.html", count = session['key_name'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)





from flask import Flask, redirect, render_template, session

app = Flask(__name__)

@app.route('/')
def index():
    number = 8
    return render_template('index.html', number=number, num2=0, color1='', color2='')

@app.route('/4')
def four():
    return render_template('index.html', number=4, num2=0, color1='', color2='')

@app.route('/<int:x>/<int:y>')
def bynum(x, y):
    return render_template('index.html', number=x, num2=y , color1='', color2='')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def colored(x, y, color1, color2):
    return render_template('index.html', number=x, num2=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
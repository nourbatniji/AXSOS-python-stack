from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play1():
    return render_template("index.html", number = 0, color="")

@app.route('/play/<int:number>')
def play2(number):
    return render_template("index.html", number = number)

@app.route('/play/<int:number>/<color>')
def play3(number, color):
    return render_template("index.html", number = number, color = color)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/Champion')
def champion():
    return "Champion"

@app.route("/say/<word>")
def say(word):
    return "Hi " + word

@app.route("/repeat/<int:number>/<name>")
def repeat(number, name):
    return number * (" "+ name)
 
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404 

if __name__ == "__main__":
    app.run(debug=True)
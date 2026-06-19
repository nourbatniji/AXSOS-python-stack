from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def display_form():
    username = request.form['username']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("display.html", username=username, location=location, language=language, comment=comment)

if __name__ == "__main__":
    app.run(debug=True, port = 5001)
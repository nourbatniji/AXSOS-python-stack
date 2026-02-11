from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render():
    student_info =[
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template('index.html', students_info = student_info, random_numbers = [9, 8, 3])

if __name__ == '__main__':
    app.run(debug=True)
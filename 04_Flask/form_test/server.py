from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/users', methods=['POST'])

def create_user():
    print("got post info")
    print(request.form)
    session['username'] = request.form['name'] #accessing data
    session['useremail'] = request.form['email']
    return redirect("/show")  
 
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")
name_on_template=session['username']
email_on_template=session['useremail']
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

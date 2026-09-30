from flask import Flask, render_template, url_for, flash,redirect
from forms import RegistrationForm,LoginForm


app = Flask(__name__)
app.config['SECRET_KEY']='be43c68e374426231eaee27462438213'

posts = [
    {'author': 'Cprey Schafer',
     'title':'Blog Post 1',
     'content':'First post content',
     'posted_on': 'April 21, 2018',},
    {'author': 'Lin Ling',
     'title': 'Blog Post 2',
     'content': 'First post content',
     'posted_on': 'April 21, 2025', }
]





@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def create():
    return render_template('about.html')
@app.route("/register", methods=["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title = 'Register', form =form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form =form)

if __name__ == '__main__':
    app.run(debug=True)
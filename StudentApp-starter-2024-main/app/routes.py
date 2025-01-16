from app import app
from flask import render_template
from app.forms import LoginForm, RegisterForm
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
    


@app.route('/events', methods=['GET', 'POST'])
def events():
    return render_template('events.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   return render_template('login.html', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegisterForm()
   return render_template('register.html', form = form)

from app import app
from flask import render_template

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
    


@app.route('/events', methods=['GET', 'POST'])
def events():
    return render_template('events.html')

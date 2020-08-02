"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from instagram import getfollowedby, getname
from mathgames import pythagorean_game, get_random_numbers, get_random_operator, operation_game


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Session control"""
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        if request.method == 'POST':
            username = getname(request.form['username'])
            return render_template('index.html', data=getfollowedby(username))
        return render_template('index.html')


@app.route('/game', methods=['GET','POST'])
def game():
    """Game control"""
    if session.get('logged_in'):
        return render_template('game.html')
    else:
        return render_template('index.html')


@app.route('/game/pythaggame', methods=['GET', 'POST'])
def pygame_start():
    a,b = get_random_numbers()
    return render_template('pythaggame.html', number=[a,b])


@app.route('/game/pythaggame_update', methods=['POST'])
def pygame_update():
    hypot = request.data
    print(type(hypot))
    data_str = hypot.decode('utf8')
    data_list = data_str.split(',')
    print(data_list)

    print("********")
    # content = hypot.get_json()
    # get_jsonprint(content)

    calculation_data = pythagorean_game(int(data_list[0].replace('"', '')), int(data_list[1]), int(data_list[2].replace('"', '')))
    return calculation_data


@app.route('/game/operationgame', methods=['GET', 'POST'])
def opgame_start():
    a, b = get_random_numbers()
    c = get_random_operator()
    return render_template('operationgame.html', number=[a, b, c])


@app.route('/quiz')
def quiz():
    """Quiz control"""
    if session.get('logged_in'):
        return render_template('quiz.html')
    else:
        return render_template('index.html')


@app.route('/quiz/algQuiz')
def algQuiz():
    if session.get('logged_in'):
        return render_template('algQuiz.html')
    else:
        return render_template('index.html')


@app.route('/lesson')
def lesson():
    """Lesson Page"""
    if session.get('logged_in'):

        return render_template('lesson.html')
    else:
        return render_template('index.html')


@app.route('/about', methods=['GET','POST'])
def about():
    """About Page"""
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                return render_template('login.html', data="Login Failed: Invalid Username or Password")

        except:
            return render_template('login.html', data="Login Failed: Invalid Username or Password")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        try:
            new_user = User(
                username=request.form['username'],
                password=request.form['password'])
            db.session.add(new_user)
            db.session.commit()
        except:
            return render_template('register.html', data= "User already exists")

        return render_template('login.html')
    return render_template('register.html')


@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.secret_key = "123"
    app.run(host='0.0.0.0')

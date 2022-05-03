from logging.handlers import RotatingFileHandler
from time import sleep
from venv import create
import psycopg2
from flask import Flask, render_template, request, redirect, session
import os
import bcrypt


DATABASE_URL = os.environ.get('DATABASE_URL', 'dbname=project2db')
SECRET_KEY = os.environ.get('SECRET_KEY', 'pretend secret key for testing')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/moodlog')
def moodlog():
     # connection variable to cnnect to database
    
    DATABASE_URL=os.environ.get('HEROKU_POSTGRESQL_CRIMSON_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('SELECT id, name, mood_rating, diet_rating, sleep_rating, created_on::timestamp FROM moods_diet_sleep ORDER BY created_on DESC;')
    results = cur.fetchall()

    names = []
    mood_rating = []
    diet_rating = []
    sleep_rating = []
    created_on = []

    for column in results: 

        # column 1 is names


        names.append(column[1])
        mood_rating.append(column[2])
        diet_rating.append(column[3])
        sleep_rating.append(column[4])
        created_on.append(column[5])

    length = len(names)

    return render_template('moodlog.html', names = names, mood_rating = mood_rating, diet_rating = diet_rating, sleep_rating= sleep_rating, length = length, created_on = created_on,username = session.get('username'))

@app.route('/')
def index():
   

    return render_template('index.html',  username = session.get('username'))


@app.route('/add_mood_items',  methods=['POST'])
def add_mood_items():

    name = request.form.get("name")
    mood_rating = request.form.get("mood_rating")
    diet_rating = request.form.get("diet_rating")
    sleep_rating = request.form.get("sleep_rating")

    emotions = request.form.getlist("emotions")

    print(emotions)
   
    DATABASE_URL=os.environ.get('HEROKU_POSTGRESQL_CRIMSON_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('INSERT INTO moods_diet_sleep(name, mood_rating, diet_rating, sleep_rating) VALUES(%s,%s, %s, %s)', [name, mood_rating, diet_rating, sleep_rating])

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/login')
def login():
    
    return render_template('login.html', username = session.get('username'))



@app.route('/login', methods=['POST'])
def login_action():

    email= request.form.get('email')
    password = request.form.get('password')
    
    DATABASE_URL=os.environ.get('HEROKU_POSTGRESQL_CRIMSON_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('SELECT username, email, password_hash FROM users WHERE email = %s', [email])
    results = cur.fetchone()
    print(f'results {results}')

    password_hash = results[2]
    
    valid = bcrypt.checkpw(password.encode(), password_hash.encode())

    print(f'valid {valid}')
    # if email is not in the results, return to login

    if valid == True :
        

        return redirect('/moodlog')
    
    else:
    
        return redirect('/login')

@app.route('/sign_up', methods = ['POST'])
def signup():

    username = request.form.get('signup_username')
    email = request.form.get('signup_email')
    password = request.form.get('signup_password')

    password_hashed = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

    DATABASE_URL=os.environ.get('HEROKU_POSTGRESQL_CRIMSON_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    cur.execute('INSERT INTO users (username, email, password_hash VALUES (%s, %s, %s', [username, email, password_hashed])

    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
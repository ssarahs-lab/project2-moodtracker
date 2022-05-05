from logging.handlers import RotatingFileHandler
from time import sleep
from unittest import result
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

    username = session.get('username')
    
    DATABASE_URL=os.environ.get('DATABASE_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # find the user_id in the table, based on the username
    cur.execute('SELECT user_id FROM users where username = %s', [username])
    result = cur.fetchone()

    if result == None:
    
        return render_template('error.html')

    else:

        user_id =result[0]

    # find the moodlog of user, based on userid
    cur.execute('SELECT  name, mood_rating, diet_rating, sleep_rating, created_on::timestamp FROM moods_diet_sleep where id = %s ORDER BY created_on DESC;', [user_id])
    results = cur.fetchall()

    print(f'results {results}')
    names = []
    mood_rating = []
    diet_rating = []
    sleep_rating = []
    created_on = []

    for column in results: 
        
        names.append(column[0])
        mood_rating.append(column[1])
        diet_rating.append(column[2])
        sleep_rating.append(column[3])
        created_on.append(column[4])

    length = len(names)

    print(f'mood_rating{mood_rating}')
    print(f'created_on{created_on}')

    cur.execute("SELECT  trim(emotions::text, '{{}}') FROM moods where id = %s ORDER BY created_on DESC;", [user_id])
    mood_results = cur.fetchall()
    emotions = []

    for moodcolumn in mood_results:

        emotions.append(moodcolumn[0])

    print(emotions)

    
    return render_template('moodlog.html', names = names, mood_rating = mood_rating, diet_rating = diet_rating, sleep_rating = sleep_rating, length = length, created_on = created_on,emotions = emotions, username = session.get('username'))

@app.route('/')
def index():
   

    return render_template('index.html',  username = session.get('username'))


@app.route('/add_mood_items',  methods=['POST'])
def add_mood_items():



    username = session.get('username')

    DATABASE_URL=os.environ.get('DATABASE_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('SELECT user_id FROM users WHERE username = %s', [username])
    results = cur.fetchall()

    print(f'line 65 results {results}')

    cur.execute('SELECT user_id FROM users where username = %s', [username])
    user_id = cur.fetchone()

    print(f'userid {user_id}')


    mood_rating = request.form.get("mood_rating")
    diet_rating = request.form.get("diet_rating")
    sleep_rating = request.form.get("sleep_rating")

    emotions = request.form.getlist("emotions")

    print(emotions)
   
    DATABASE_URL=os.environ.get('DATABASE_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('INSERT INTO moods_diet_sleep(id, mood_rating, diet_rating, sleep_rating) VALUES(%s, %s, %s, %s)', [ user_id, mood_rating, diet_rating, sleep_rating])

    conn.commit()
    

    cur.execute('INSERT INTO moods(id, mood_rating, emotions) VALUES(%s, %s, %s)', [user_id, mood_rating, emotions])

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/login')
def login():
    
    return render_template('login.html', username = session.get('username'))

# login route

@app.route('/login', methods=['POST'])
def login_action():

    email= request.form.get('email')
    password = request.form.get('password')
    
    DATABASE_URL=os.environ.get('DATABASE_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('SELECT username, email, password_hash FROM users WHERE email = %s', [email])
    results = cur.fetchone()
    print(f'results {results}')

    username = results[0]

    password_hash = results[2]
    
    valid = bcrypt.checkpw(password.encode(), password_hash.encode())

    print(f'valid {valid}')
    # if email is not in the results, return to login
    if results == None:


        invalid_message = "Invalid username or password, please try again."
        return render_template ('/login', invalid_message = invalid_message)

    elif valid == True :

        session['username'] = username

        return redirect('/moodlog')
    
    else:
    
        return redirect('/login')

# sign up route

@app.route('/sign_up', methods = ['POST'])
def signup():

    username = request.form.get('signup_username')
    email = request.form.get('signup_email')
    password = request.form.get('signup_password')

    password_hashed = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

    DATABASE_URL=os.environ.get('DATABASE_URL','dbname = moodtracker')

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    cur.execute('INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)', [username, email, password_hashed])

    conn.commit()
    conn.close()

    return redirect('/')

# logout route - clears the session cookies from page and redirects

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)
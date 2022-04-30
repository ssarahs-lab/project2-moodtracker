from time import sleep
from venv import create
import psycopg2
from flask import Flask, render_template, request, redirect, session
import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'dbname=project2db')
SECRET_KEY = os.environ.get('SECRET_KEY', 'pretend secret key for testing')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    # connection variable to cnnect to database
    conn = psycopg2.connect('dbname = moodtracker')
    cur = conn.cursor()
    cur.execute('SELECT id, name, mood_rating, diet_rating, sleep_rating, created_on::timestamp FROM moods_diet_sleep;')
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

    return render_template('index.html', names = names, mood_rating = mood_rating, diet_rating = diet_rating, sleep_rating= sleep_rating, length = length, created_on = created_on, username = session.get('username'))


@app.route('/add_mood_items',  methods=['POST'])
def add_mood_items():

    name = request.form.get("name")
    mood_rating = request.form.get("mood_rating")
    diet_rating = request.form.get("diet_rating")
    sleep_rating = request.form.get("sleep_rating")
   
    conn = psycopg2.connect('dbname = moodtracker')
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
    username = request.form.get('username')
    password = request.form.get('password')
    

    emails_fromsql = []
    usernames_fromsql = []

    conn = psycopg2.connect('dbname = moodtracker')
    cur = conn.cursor()
    cur.execute('SELECT username, email, password_hash FROM users;')
    results_fetch = cur.fetchall()

    for column in results_fetch: 

        emails_fromsql.append(column[1])
        usernames_fromsql.append(column[0])
   
    print(emails_fromsql)

    # username = usernames_fromsql

    cur.execute(f"SELECT name FROM users WHERE email like '{email}' ;")
    username = cur.fetchone()

    print(username[0])

    if email in emails_fromsql:

        session['email'] = email
        session['username'] = username[0]

        # Check if this is a valid email (in the database)
        # If valid - set the user ID in session and redirect
        
        return redirect('/')

   
        # If not, redirect back to the login page.
    else:

        return redirect('/login', ) 




if __name__ == '__main__':
    app.run(debug=True)
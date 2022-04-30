from time import sleep
from venv import create
import psycopg2
from flask import Flask, render_template, request, redirect
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
    
    print(results)
    names = []
    mood_rating = []
    diet_rating = []
    sleep_rating = []
    created_on = []
    id = []

    for column in results: 

        # column 1 is names


        names.append(column[1])
        mood_rating.append(column[2])
        diet_rating.append(column[3])
        sleep_rating.append(column[4])
        created_on.append(column[5])
       
    
    print(f"names{names} +moodrating{mood_rating} + dietrating{diet_rating} + sleeprating{sleep_rating} +createdon{created_on}")

    length = len(names)

    return render_template('index.html', names = names, mood_rating = mood_rating, diet_rating = diet_rating, sleep_rating= sleep_rating, length = length, created_on = created_on)


@app.route('/add_mood_items',  methods=['POST'])
def add_mood_items():

    name = request.form.get("name")
    mood_rating = request.form.get("mood_rating")
    diet_rating = request.form.get("diet_rating")
    sleep_rating = request.form.get("sleep_rating")
    
    

    print(f'{name}+{mood_rating}+{diet_rating}+{sleep_rating}')

    conn = psycopg2.connect('dbname = moodtracker')
    cur = conn.cursor()
    cur.execute('INSERT INTO moods_diet_sleep(name, mood_rating, diet_rating, sleep_rating) VALUES(%s,%s, %s, %s)', [name, mood_rating, diet_rating, sleep_rating])

    conn.commit()
    conn.close()



    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
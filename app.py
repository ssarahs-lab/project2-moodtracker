from flask import Flask, render_template, request, redirect
import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'dbname=project2db')
SECRET_KEY = os.environ.get('SECRET_KEY', 'pretend secret key for testing')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/add_food_items',  methods=['POST'])
def add_food_items():

    name = request.form.get("name")
    mood_rating = request.form.get("mood_rating")
    diet_rating = request.form.get("diet_rating")

    print(f'{name}+{mood_rating}+{diet_rating}')

    conn = psycopg2.connect('dbname = moodtracker')
    cur = conn.cursor()
    cur.execute('INSERT INTO food(name, price_in_cents, image_url) VALUES(%s, %s, %s)', [name, price, image_url])

    conn.commit()
    conn.close()



    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
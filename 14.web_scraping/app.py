from flask import Flask, render_template, redirect, url_for
from database import Database
from movie import get_movie_data


app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    query = "SELECT * FROM movie_data"
    result = db.execute_fetch(query)
    return render_template('index.html', result=result)

@app.route('/update')
def update():
    movie_data = get_movie_data()
    for d in movie_data:
        name = d['name']
        grade = d['grade']
        reservation_percente = d['reservation_percente']
        img_url = d['img_url']
        short_summary = d['short_summary']
        
        sql = "INSERT INTO movie_data(name, grade, reservation_percente, img_url, short_summary) VALUES(?, ?, ?, ?, ?)"
        db.execute(sql, (name, grade, reservation_percente, img_url, short_summary))
    db.commit()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True, port=8008)
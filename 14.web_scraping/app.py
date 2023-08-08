from flask import Flask, render_template, redirect, url_for
from database import Database
from movie import get_movie_ranking_data


app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    query = "SELECT * FROM movie_data;"
    result = db.execute_fetch(query)
    datas = []
    for d in result:
        d = {
            'id': d[0], 
            'name': d[1], 
            'grade': d[2],
            'reservation_percente': d[3], 
            'img_url': d[4], 
            'short_summary': d[5], 
            'url': d[6]
        }
        datas.append(d)
    return render_template('index.html', datas=datas)

@app.route('/movie_daily_ranking')
def movie_daily_ranking():
    query = "SELECT DISTINCT date FROM daily_movie_ranking;"
    result = db.execute_fetch(query)
    datas = []
    for d in result:
        d = {'date': d[0]}
        datas.append(d)
    return render_template('day_list.html', datas=datas)

@app.route('/movie_daily_ranking/<date>')
def movie_daily_ranking_detail(date):
    query = '''
        SELECT daily_movie_ranking.ranking, movie_data.name, movie_data.grade, movie_data.reservation_percente, movie_data.img_url, 
               movie_data.short_summary, movie_data.url
        FROM daily_movie_ranking
        JOIN movie_data ON daily_movie_ranking.movie_id = movie_data.id
        WHERE date=?
        ORDER BY daily_movie_ranking.ranking ASC;
    '''
    result = db.execute_fetch(query, (date,))
    
    datas = []
    for d in result:
        d = {
            'ranking': d[0],
            'name': d[1],
            'grade': d[2],
            'reservation_percente': d[3],
            'img_url': d[4],
            'short_summary': d[5],
            'url': d[6]
        }
        datas.append(d)
    return render_template('movie_daily_ranking.html', date=date, datas=datas)

@app.route('/update')
def update():
    movie_data = get_movie_ranking_data()
    for d in movie_data:
        name = d['name']
        grade = d['grade']
        reservation_percente = d['reservation_percente'].replace("%", "")
        img_url = d['img_url']
        short_summary = d['short_summary']
        url = d['url']
        ranking = d['ranking']
        today_date = d['today_date']
        
        # movie_data 추가
        query = "SELECT * FROM movie_data WHERE name=?;"
        movie = db.execute_fetch(query, (name,))
        if movie is None:
            query = "INSERT INTO movie_data(name, grade, reservation_percente, img_url, short_summary, url) VALUES(?, ?, ?, ?, ?, ?);"
            db.execute(query, (name, grade, reservation_percente, img_url, short_summary, url))

        # daily_movie_ranking 추가
        query = '''
            SELECT *
            FROM daily_movie_ranking
            JOIN movie_data ON daily_movie_ranking.movie_id = movie_data.id
            WHERE movie_data.name=? AND daily_movie_ranking.date=?;
        '''
        movie_ranking = db.execute_fetch(query, (name, today_date))
        if movie_ranking is None:
            query = "SELECT id FROM movie_data WHERE name=?;"
            movie_id = db.execute_fetch(query, (name,))[0][0]
            query = "INSERT INTO daily_movie_ranking(date, movie_id, ranking) VALUES(?, ?, ?);"
            db.execute(query, (today_date, movie_id, ranking))
        
    db.commit()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True, port=8008)
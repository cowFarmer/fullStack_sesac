from flask import Flask, render_template, request
from database import Database


app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    title = request.form['title']
    message = request.form['text']
    
    sql = f"INSERT INTO board(title, message) VALUES('{title}', '{message}')"
    db.execute(sql)
    db.commit()
    return "OK"

@app.route('/list')
def list():
    sql = "SELECT * FROM board"
    result = db.execute_fetch(sql)
    header = ['id', 'title', 'message']
    
    dict_result = []
    for i in range(len(result)):
        dict_result.append(dict(zip(header, result[i])))
    
    return dict_result

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']
    
    sql = f"DELETE FROM board WHERE id='{id}'"
    db.execute(sql)
    db.commit()
    return ""

@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    title = request.form['title']
    message = request.form['message']
    
    sql = f"UPDATE board SET title='{title}', message='{message}' WHERE id='{id}'"
    db.execute(sql)
    db.commit()
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=8888)
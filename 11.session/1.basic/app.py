from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import json


app = Flask(__name__)
app.secret_key = "SESAC"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sessions.db"
db = SQLAlchemy(app)

app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db
Session(app)

# 세션 저장을 위한 DB 저장소 설계
class SessionData(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    data = db.Column(db.Text)

# 원하는 데이터 내용을 DB의 data에 변수 저장
def session_store(sid, data):
    session_data = SessionData.query.get(sid)
    if not session_data:
        session_data = SessionData(id=sid)
    
    # human readable type은 늘 좋은 건 아님
    # 과거엔 binary로 많이 보냈는데, tradeoff가 있음
    # 유지보수의 장점이 있지만, 해킹시 민감 데이터 바로 노출되는 단점이 있음
    session_data.data = json.dumps(data)
    db.session.add(session_data)
    db.session.commit()
    
# 세션 데이터 가져오는 함수
def get_session_data(sid):
    session_data = SessionData.query.get(sid)
    if session_data:
        return json.loads(session_data.data)
    return {}

@app.route("/")
def index():
    session["username"] = "user"
    session["data"] = ""
    
    session["count"] = 42
    session["my_list"] = [1, 2, 3, 4, 5]
    
    session_store(session.sid, dict(session))
    return "hello"

@app.route("/get_session")
def get_session():
    username = session.get("username")
    data = session.get("data")
    
    # 저장된 데이터 가져오기
    stored_session_data = get_session_data(session.sid)
    print(stored_session_data)
    
    stored_session_str = json.dumps(stored_session_data, indent=4)
    print(stored_session_str)
    return f"{username}, {data}"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8989)
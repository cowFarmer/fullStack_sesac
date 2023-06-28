from flask import Flask, render_template, redirect, url_for
from users import get_user

app = Flask(__name__)

@app.route('/')
def home():
    user_names = ["alice", "bob", "joe", "david", "eve", "admin"]
    return render_template("index.html", username=user_names)

@app.route('/user')
def users():
    return render_template("user.html", username=get_user())
    

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
# 미션1. 사용자 이름을 우리의 csv 파일로 대체하기
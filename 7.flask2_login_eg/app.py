from flask import Flask, render_template
from flask import request, redirect, session, url_for
from flask import flash

from datetime import timedelta


app = Flask(__name__)

app.secret_key = "sesac_secret_key"
app.permanent_session_lifetime = timedelta(minutes=1)

# 가상의 사용자 테이블
users = {
    "user1": {"password": "password123"},
    "user2": {"password": "abc123"},
    "sesac": {"password": "sesac"}
}

@app.route("/home")
@app.route("/")
def home():
    if "username" in session:
        username = session["username"]
        return render_template("home.html", username=username)
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username]["password"] == password:
            session["username"] = username
            flash("성공적으로 로그인 되었습니다.", "primary")
            # return redirect(url_for("home"))
        else:
            flash("다시 시도해 주십시오.", "danger")
        
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
    
# 미션 1. 랜더 템플릿 통해 첫 화면에 login, logout 추가
# 미션 2. 로그인 성공 실패 여부를 flash 메세지로 처리
# 미션 3. 디자인 적용해서 flask 메세지 색상 다르게 하기(성공 초록, 실패 빨강)
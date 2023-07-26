from flask import Flask, render_template
from flask import request, redirect, session, url_for
from flask import flash
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta


app = Flask(__name__)

app.secret_key = "sesac_secret_key"
# app.permanent_session_lifetime = timedelta(minutes=1)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Users(db.Model):
    # CREATE TABLE Users (_id INTEGER PRIMARY_KEY)
    '''
    CREATE TABLE Users (
        id INTEGER PRIMARY_KEY,
        name TEXT,
        password TEXT,
        email TEXT
    )
    '''
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    

@app.route("/")
def home():
    if "username" in session:
        username = session["username"]
        return render_template("home.html", username=username)
    return render_template("home.html")

@app.route("/view")
def view():
    return render_template("view.html", users=Users.query.all())

@app.route("/delete", methods=["POST"])
def delete():
    user = session["username"]
    if request.method == "POST":
        action = request.form["action"]
        if action == "DELETE":
            Users.query.filter_by(name=user).delete()
            db.session.commit()
            return redirect(url_for("logout"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # DB를 통해 로그인 확인
        found_user = Users.query.filter_by(name=username).first()
        if found_user:
            flash("성공적으로 로그인 되었습니다.", "primary")
        else:
            user = Users(username, password, "")
            db.session.add(user)
            db.session.commit()
            flash("성공적으로 생성 되었습니다.", "primary")
        
        session["username"] = username
        return redirect(url_for("home"))
        
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port="5050")
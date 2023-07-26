from flask import Flask, render_template
from flask import request, redirect, url_for
from flask import session
from flask import flash

from datetime import timedelta


app = Flask(__name__)
app.secret_key = "sesac"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/", methods=["GET", "POST"])
@app.route("/<name>")
def home(name=""):
    name = None
    age = None
    
    if request.method == "GET":
        name = request.args.get("name")
        age = request.args.get("age")
    elif request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        session["userid"] = name
        # session.permanent = True
        flash("user name을 입력하셨습니다.")
        flash("메세지 flash 예제 입니다.")
    else:
        return "UNKOWN MEHTOD"
    
    return render_template("index.html", name=name, age=age)

@app.route("/user")
def user():
    if "userid" in session:
        user = session["userid"]
        return f"<h1>hello, {user}"
    else:
        return redirect(url_for("home"))

@app.route("/redirect")
def redirect_example():
    # return redirect("/")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
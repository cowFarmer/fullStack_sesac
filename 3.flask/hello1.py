from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1><a href="/">home</a></h1>
    <h1><a href="/user">go user</a></h1>
    <h3>this is home</h3>
    """
    
@app.route("/user")
def user_none():
    return """
    <h1><a href="/">home</a></h1>
    <h1><a href="/user">go user</a></h1>
    <h3>this is user page</h3>
    <ul>
    <li><a href="/user/john">john</a></li>
    <li><a href="/user/anna">anna</a></li>
    <li><a href="/user/홍길동">홍길동</a></li>
    </ul>
    """
    
@app.route("/user/<name>")
def user(name):
    return f"""
    <h1><a href="/">home</a></h1>
    <h1><a href="/user">go user</a></h1>
    <h3>this is {name}'s page</h3>
    """

@app.route("/admin")
def admin():
    # 응용하는 방법
    # if user is not loggedin:
    #     redirect해서 login 페이지 전달하기
    return redirect(url_for("user", name="admin"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
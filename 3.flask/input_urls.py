from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/user/<name>")
def user(name):
    return f"hello i'm {name}"

@app.route("/user/<int:age>")
def userage(age):
    return f"hello i'm {age}"

@app.route("/user/<name>/<int:age>/<float:weight>")
def userdetail(name, age, weight):
    return f"hello i'm {name}, {age}, {weight}"

if __name__ == "__main__":
    app.run()
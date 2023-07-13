from flask import Flask, render_template


app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/item")
def item():
    return render_template("item.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/order_item")
def order_item():
    return render_template("order_item.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
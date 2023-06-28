from flask import Flask, render_template
import csv

app = Flask(__name__, static_folder="static")

def get_user(id):
    with open("./csv/user.csv", "r") as file:
        lines = csv.DictReader(file)
        for line in lines:
            print(line)
            if line["Id"] == id:
                return line
    return None

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user')
def user():
    with open("./csv/user.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("main.html", users_info = lines)

@app.route('/user/<id>')
def user_info(id):
    user = get_user(id)
    return render_template("user_info.html", user_info = user)

@app.route('/store')
def store_list():
    with open("./csv/store.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("store_list.html", users_info = lines)

@app.route('/item')
def item_list():
    with open("./csv/item.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("item.html", users_info = lines)


@app.route('/order')
def order_list():
    with open("./csv/order.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("order.html", users_info = lines)


@app.route('/order_item')
def order_item_list():
    with open("./csv/orderitem.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("order_item.html", users_info = lines)
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)
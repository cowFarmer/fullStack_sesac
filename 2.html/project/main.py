from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/inventory_manager')
def inventory_manager():
    return render_template("inventory_manager.html")

@app.route('/inventory_manager/guide')
def inventory_manager_guide():
    pass

@app.route('/store_manager')
def store_manager():
    return render_template("store_manager.html")

@app.route('/shopping')
def shopping():
    return render_template("shopping.html")

@app.route('/user')
def user():
    return render_template("user.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
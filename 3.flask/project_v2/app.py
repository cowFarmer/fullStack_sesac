from flask import Flask, render_template, request, Blueprint
from utils.static_url import user_csv_file, order_csv_file, order_item_csv_file, item_csv_file, store_csv_file
from utils.controller import ReadCsvDict, CheckData
from routes.user.views import user_bp
from routes.store.views import store_bp
from routes.item.views import item_bp
from routes.order.views import order_bp
from routes.order_item.views import order_item

app = Flask(__name__, static_folder="static")

app.register_blueprint(user_bp)
app.register_blueprint(store_bp)
app.register_blueprint(item_bp)
app.register_blueprint(order_bp)
app.register_blueprint(order_item)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port=8888)
    # app.run(debug=True, port=8888, host='0.0.0.0')
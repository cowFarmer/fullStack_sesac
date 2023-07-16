from flask import Flask

# blue print
from apps.view.home_view import home_bp
from apps.view.user_view import user_bp
from apps.view.store_view import store_bp
from apps.view.item_view import item_bp
from apps.view.order_view import order_bp
from apps.view.order_item_view import order_item_bp


app = Flask(__name__, static_folder="static")

app.register_blueprint(home_bp)
app.register_blueprint(user_bp)
app.register_blueprint(store_bp)
app.register_blueprint(item_bp)
app.register_blueprint(order_bp)
app.register_blueprint(order_item_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
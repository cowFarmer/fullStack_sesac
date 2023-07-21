from flask import Flask

# blue print
from view.home_view import home_bp
from view.user_view import user_bp
from view.store_view import store_bp
from view.item_view import item_bp
from view.order_view import order_bp
from view.order_item_view import order_item_bp
from view.kiosk_view import kiosk_bp


app = Flask(__name__, static_folder="static")

app.register_blueprint(home_bp)
app.register_blueprint(user_bp)
app.register_blueprint(store_bp)
app.register_blueprint(item_bp)
app.register_blueprint(order_bp)
app.register_blueprint(order_item_bp)
app.register_blueprint(kiosk_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
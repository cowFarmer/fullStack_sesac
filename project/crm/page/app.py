from flask import Flask, render_template

# blue print
from routes.home.views import home_bp
from routes.user.views import user_bp
from routes.store.views import store_bp
from routes.item.views import item_bp
from routes.order.views import order_bp
from routes.order_item.views import order_item_bp


app = Flask(__name__, static_folder="static")

app.register_blueprint(home_bp)
app.register_blueprint(user_bp)
app.register_blueprint(store_bp)
app.register_blueprint(item_bp)
app.register_blueprint(order_bp)
app.register_blueprint(order_item_bp)







if __name__ == "__main__":
    
    app.run(debug=True, port=8080)
from view.home_view import home_bp
from view.user_view import user_bp
from view.store_view import store_bp
from view.item_view import item_bp
from view.order_view import order_bp
from view.order_item_view import order_item_bp
from view.kiosk_view import kiosk_bp

def register_bp(app):
    blueprint_list = [home_bp, user_bp, store_bp, item_bp, order_bp, order_item_bp, kiosk_bp]
    
    for bp in blueprint_list:
        app.register_blueprint(bp)
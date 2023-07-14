from flask import Blueprint, render_template


order_item_bp = Blueprint("order_item", __name__)

@order_item_bp.route("/order_item")
def order_item():
    return render_template("order_item.html")

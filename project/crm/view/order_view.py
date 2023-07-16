from flask import Blueprint, render_template


order_bp = Blueprint("order", __name__)

@order_bp.route("/order")
def order():
    return render_template("order.html")
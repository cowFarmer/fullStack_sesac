from flask import Flask, render_template, Blueprint


store_bp = Blueprint("store", __name__)

@store_bp.route("/store")
def store():
    return render_template("store.html")
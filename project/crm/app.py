from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from view.home_view import home_bp
from view.user_view import user_bp
from view.store_view import store_bp
from view.item_view import item_bp
from view.order_view import order_bp
from view.order_item_view import order_item_bp
from view.kiosk_view import kiosk_bp

import os


app = Flask(__name__, static_folder="static")
# sqlAlchemy
app.instance_path = os.path.join(os.getcwd() + "/model/database")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crm.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    gender = db.Column(db.String(16))
    age = db.Column(db.Integer())
    birthdate = db.Column(db.String(32))
    address = db.Column(db.String(64))
    
    def __repr__(self):
        return {f"id: '{self.id}', name: '{self.name}', gender: '{self.age}'"}

class Store(db.Model):
    __tablename__ = "store"
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))
    address = db.Column(db.String(64))
    
class Orderitem(db.Model):
    __tablename__ = "orderitem"
    id = db.Column(db.String(64), primary_key=True)
    orderid = db.Column(db.String(64), db.ForeignKey("order.id"))
    itemid = db.Column(db.String(64), db.ForeignKey("item.id"))

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(64))
    unitpirce = db.Column(db.Integer())
    
    def __repr__(self):
        return 
    
class Ordered(db.Model):
    __tablename__ = "ordered"
    id = db.Column(db.String(64), primary_key=True)
    orderat = db.Column(db.DateTime(64))
    storeid = db.Column(db.String(64), db.ForeignKey("store.id"))
    userid = db.Column(db.String(64), db.ForeignKey("user.id"))
    
    def __repr__(self):
        return f"id: '{self.id}', orderat: '{self.orderat}', storeid: '{self.storeid}', userid: '{self.userid}'"

blueprint_list = [home_bp, user_bp, store_bp, item_bp, order_bp, order_item_bp, kiosk_bp]

for blueprint in blueprint_list:
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        test = User.query.all()
        print(test)
        
    
    app.run(debug=True, port=8080)
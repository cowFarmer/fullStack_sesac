from app import db


# Table Definition
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    gender = db.Column(db.String(16))
    age = db.Column(db.Integer())
    birthdate = db.Column(db.String(32))
    address = db.Column(db.String(64))

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
    
class Ordered(db.Model):
    __tablename__ = "ordered"
    id = db.Column(db.String(64), primary_key=True)
    orderat = db.Column(db.DateTime(64))
    storeid = db.Column(db.String(64), db.ForeignKey("store.id"))
    userid = db.Column(db.String(64), db.ForeignKey("user.id"))
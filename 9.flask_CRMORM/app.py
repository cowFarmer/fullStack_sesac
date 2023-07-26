from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)

app.instance_path = os.getcwd()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user-sample.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    # 테이블 이름 정의
    __tablename__ = 'users'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    age = db.Column(db.Integer())
    birthdate = db.Column(db.String(32))
    address = db.Column(db.String(64))
    
    # relation
    orderR = db.relationship("Order", backref="users")
    
    def __repr__(self):
        return f"<User {self.name}, {self.gender}, {self.age}, {self.birthdate}, {self.address}>"

class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))
    address = db.Column(db.String(64))
    
    # relation
    orderR = db.relationship("Order", backref="stores")
    
    def __repr__(self):
        return f"<Store {self.name}, {self.type}, {self.address}>"

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.String(64), primary_key=True)
    orderat = db.Column(db.String(64))
    storeid = db.Column(db.String(64), db.ForeignKey('stores.id'))
    userid = db.Column(db.String(64), db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f"<order {self.id}, {self.orderat}"

@app.route("/")
def home():
    # users = User.query.filter_by(name="윤수빈").all()
    # stores = Store.query.all()
    # orders = Order.query.all()
    
    # users = User.query.filter_by(name="윤수빈").first()
    # order_by_user = users.orderR
    # print(order_by_user)
    
    
    # 미션1. 윤수빈이 방문한 상점명 SQL로 출력하기
    # query = f'''
    # SELECT users.Id, stores.Name
    # FROM users
    # JOIN orders ON users.Id = orders.UserId
    # JOIN stores ON orders.StoreId = stores.Id
    # WHERE orders.UserId = (
    #     SELECT users.id
    #     FROM users
    #     WHERE users.name = "윤수빈"
    #     LIMIT 1
    # );
    # '''
    
    # 미션1-1. 윤수빈이 방문한 상점명 join 이용해서 출력하기
    user_id = db.session.query(User.id).filter(User.name=="윤수빈").first()[0]
    users_order_stores = db.session.query(User.id, User.name, Store.name) \
        .join(Order, User.id == Order.userid) \
        .join(Store, Order.storeid == Store.id) \
        .filter(User.id == user_id).all()

    for d in users_order_stores:
        print(d)
    
    # users = User.query.filter_by(name="윤수빈").first()
    # order_by_user = users.orderR
    
    # for order in order_by_user:
    #     store = order.stores
    #     print(f"윤수빈이 방문한 상점은 {store.name}")
    
    return "Hello"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(port="8888", debug=True)
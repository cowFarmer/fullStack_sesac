from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate


"""
LoginManager: 로그인 관리를 담당하는 클래스로, Flask 애플리케이션에서 로그인 기능을 초기화하고 관리하는 역할을 합니다.
UserMixin: UserMixin 클래스는 Flask-Login이 기본적으로 사용하는 사용자 모델 클래스를 정의하기 위해 사용됩니다. 이 클래스를 사용하여 사용자 모델 클래스에 필요한 메서드들을 간단하게 추가할 수 있습니다.
login_user: 로그인 처리를 위해 사용되는 함수로, 인증이 성공적으로 완료된 사용자를 로그인 상태로 만듭니다. 이 함수를 호출하면 세션에 사용자 정보가 저장되어 사용자를 인증된 상태로 유지할 수 있습니다.
login_required: 데코레이터로, 특정 뷰 함수를 보호하는 데 사용됩니다. 이 데코레이터가 적용된 뷰 함수는 로그인된 사용자만 접근할 수 있으며, 로그인되지 않은 사용자는 로그인 페이지로 리디렉션됩니다.
logout_user: 로그아웃 처리를 위해 사용되는 함수로, 현재 로그인된 사용자를 로그아웃 상태로 만듭니다. 세션에서 사용자 정보를 삭제하여 인증을 끝내는 역할을 합니다.
current_user: 현재 로그인된 사용자를 나타내는 객체입니다. 로그인되지 않은 경우 AnonymousUserMixin 객체가 반환됩니다. 이를 통해 로그인된 사용자의 정보를 뷰 함수에서 간단하게 접근할 수 있습니다.
"""

app = Flask(__name__)

app.config['SECRET_KEY'] = "sesac"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# DB 생성
db = SQLAlchemy(app)

# DB migration 모듈 로딩
migrate = Migrate(app, db)

# 로그인 매니저 생성
login_manager = LoginManager(app)
login_manager.login_view = "login" # 로그인 페이지 URI 명시

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), nullable=True)
    
    def set_password(self, password):
        # self.password = password
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        # return self.password == password
        return check_password_hash(self.password_hash, password)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def main():
    return render_template("main.html", current_user=current_user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter(User.username==username).first()
        if user and user.check_password(password):
            flash("로그인에 성공 했습니다", "primary")
            login_user(user)
        else:
            flash("로그인에 실패했습니다.", "danger")
    return redirect(url_for("main"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main"))

@app.route("/profile_edit", methods=["GET", "POST"])
@login_required
def profile_edit():
    if request.method == "POST":
        new_password = request.form["new_password"]
        current_user.set_password(new_password)
        db.session.commit()
        flash("성공적으로 수정 되었습니다.", "success")
        return redirect(url_for("main"))
    return render_template("profile_edit.html", current_user=current_user)

@app.route("/profile_delete", methods=["POST"])
@login_required
def profile_delete():
    if request.method == "POST":
        user = User.query.filter_by(username=current_user.username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            flash("성공적으로 삭제 되었습니다.", "danger")
            return redirect(url_for("main"))
    return render_template("profile_edit.html", current_user=current_user)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "사용자가 이미 존재합니다."
        # new_user = User(username=username)
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("성공적으로 생성 되었습니다.", "info")
        return redirect(url_for("main"))
    return render_template("register.html", current_user=current_user)

@app.route("/users")
@login_required
def view_users():
    users = User.query.all()
    return render_template("users.html", users=users, current_user=current_user)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True, port=8008)
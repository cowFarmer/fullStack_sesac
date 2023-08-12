from flask import Flask, render_template, redirect, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests, random, string, enum, datetime, jwt, uuid


app = Flask(__name__)
app.secret_key = open("./secret/app_secret_key.txt", "r").read()

login_manager = LoginManager(app)
login_manager.login_view = "login"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///today-exhibition.db"
db = SQLAlchemy(app)

app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db
app.config["SESSION_COOKIE_NAME"] = "TE_SES"
Session(app)

class LoginType(enum.Enum):
    NAVER = "NAVER"
    KAKAO = "KAKAO"

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(64), primary_key=True)
    # password = db.Column(db.String(64))
    email = db.Column(db.String(32))
    nickname = db.Column(db.String(16), nullable=False)
    profile_img = db.Column(db.String(256))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)
    gender = db.Column(db.String(6))
    birthdate = db.Column(db.Date())
    login_type = db.Column(db.Enum(LoginType), nullable=False)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    # 현재는 session_data의 유무로 보고 있지만, db랑 조회하는 방식으로 가야하나?
    if not "_user_id" in session:
        if 'naver_login' in request.form:
            NAVER_CLIENT_ID = open("./secret/naver_client_id.txt", "r").read()
            callback_url = "http://localhost:8888/naver/callback"
            url = f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={NAVER_CLIENT_ID}&redirect_uri={callback_url}"
            
            # naver 검증용 state(optional)
            # state = ''.join(random.choice(string.ascii_letters) for _ in range(16))
            # url = f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={NAVER_CLIENT_ID}&redirect_uri={callback_url}&state={state}"
            return redirect(url)
        if 'kakao_login' in request.form:
            KAKAO_CLIENT_ID = open("./secret/kakao_client_id.txt", "r").read()
            callback_url = "http://localhost:8888/kakao/callback"
            url = f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={KAKAO_CLIENT_ID}&redirect_uri={callback_url}"
            return redirect(url)
    else:
        return redirect(url_for('whoami'))
    
@app.route('/naver/callback')
def naver_callback():
    # 네이버
    NAVER_CLIENT_ID = open("./secret/naver_client_id.txt", "r").read()
    NAVER_CLIENT_SECRET = open("./secret/naver_client_secret.txt", "r").read()
    
    params = request.args.to_dict()
    code = params.get("code")
    state = params.get("state")
    
    token_request = requests.get(f"https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id={NAVER_CLIENT_ID}&client_secret={NAVER_CLIENT_SECRET}&code={code}&state={state}")
    token_json = token_request.json()
    
    return ""

@app.route('/kakao/callback')
def kakao_callback():
    # 카카오
    KAKAO_CLIENT_ID = open("./secret/kakao_client_id.txt", "r").read()
    KAKAO_CLIENT_SECRET = open("./secret/kakao_client_secret.txt", "r").read()
    
    params = request.args.to_dict()
    code = params.get("code")
    
    callback_url = "http://localhost:8888/kakao/callback"    
    
    token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={KAKAO_CLIENT_ID}&client_secret={KAKAO_CLIENT_SECRET}&redirect_uri={callback_url}&code={code}")
    token_json = token_request.json()
    ACCESS_TOKEN = token_json.get("access_token")
    profile_request = requests.get(f"https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
    data = profile_request.json()
    
    return social_signin(data, "kakao")

@app.route('/whoami')
def whoami():
    user_id = session.get("_user_id")
    user = User.query.filter_by(id=user_id).first()
    return f"<h1>hi {user.nickname}</h1>"

@login_manager.user_loader
def load_user(user_id):
    return ""

def social_signin(data, type):
    if type == "kakao":
        kakao_account = data.get("kakao_account")
        profile = kakao_account.get("profile")
        email = kakao_account.get("email")
        
        # 이메일로 검증
        user = User.query.filter_by(email=email).first()
        if not user:
            new_user = User(
                id = str(uuid.uuid4()),
                # password는 넣지 않는거로...
                # password = str(data.get("id")),
                email = email,
                nickname = profile.get("nickname"),
                profile_img = profile.get("profile_image_url"),
                created_at = datetime.datetime.now(),
                gender = kakao_account.get("gender"),
                # 카카오 birthdate는 월, 일만 받아오는 이슈 있음
                # birthdate = None,
                login_type = LoginType.KAKAO
            )
        
            db.session.add(new_user)
            db.session.commit()
        
        user_id = db.session.query(User.id).filter_by(email=email).first()[0]
        if user_id:
            user = User.query.get(user_id)
            login_user(user)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8888)
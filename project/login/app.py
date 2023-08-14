from flask import Flask, render_template, redirect, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import requests, enum, datetime, uuid


app = Flask(__name__)
app.secret_key = open("./secret/app_secret_key.txt", "r").read()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///today-exhibition.db"
db = SQLAlchemy(app)

app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db
Session(app)

class LoginType(enum.Enum):
    NAVER = "NAVER"
    KAKAO = "KAKAO"

class User(db.Model):
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
    
    def __repr__(self):
        return f'{self.id},{self.email}{self.nickname}{self.profile_img}{self.created_at}{self.gender}{self.birthdate}{self.login_type}'

@app.route('/')
def index():
    if "user_id" in session:
        user_id = session.get("user_id")
        return render_template("main.html", user_id=user_id)
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    # 현재는 session_data의 유무로 보고 있지만, db랑 조회하는 방식으로 가야하나?
    if not "user_id" in session:
        if "naver_login" in request.form:
            NAVER_CLIENT_ID = open("./secret/naver_client_id.txt", "r").read()
            
            callback_url = "http://127.0.0.1:8000/naver/callback"
            url = f"https://nid.naver.com/oauth2.0/authorize?client_id={NAVER_CLIENT_ID}&response_type=code&redirect_uri={callback_url}"
            
            # naver 검증용 state(optional)
            # state = ''.join(random.choice(string.ascii_letters) for _ in range(16))
            # url = f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={NAVER_CLIENT_ID}&redirect_uri={callback_url}&state={state}"
            return redirect(url)
        
        if "kakao_login" in request.form:
            KAKAO_CLIENT_ID = open("./secret/kakao_client_id.txt", "r").read()
            callback_url = "http://127.0.0.1:8000/kakao/callback"
            url = f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={KAKAO_CLIENT_ID}&redirect_uri={callback_url}"
            return redirect(url)
    else:
        return redirect(url_for('whoami'))

@app.route('/logout', methods=['POST'])
def logout():
    if "user_id" in session:
        session.clear()
    return redirect(url_for('index'))
    
@app.route('/naver/callback')
def naver_callback():
    # 네이버
    NAVER_CLIENT_ID = open("./secret/naver_client_id.txt", "r").read()
    NAVER_CLIENT_SECRET = open("./secret/naver_client_secret.txt", "r").read()
    
    params = request.args.to_dict()
    code = params.get("code")
    
    token_request = requests.get(f"https://nid.naver.com/oauth2.0/token?client_id={NAVER_CLIENT_ID}&client_secret={NAVER_CLIENT_SECRET}&grant_type=authorization_code&code={code}")
    token_json = token_request.json()
    ACCESS_TOKEN = token_json.get("access_token")
    TOKEN_TYPE = token_json.get("token_type")
    profile_request = requests.get(f"https://openapi.naver.com/v1/nid/me", headers={"Authorization": f"{TOKEN_TYPE} {ACCESS_TOKEN}"})
    data = profile_request.json()
    return social_signin(data, "naver")

@app.route('/kakao/callback')
def kakao_callback():
    # 카카오
    KAKAO_CLIENT_ID = open("./secret/kakao_client_id.txt", "r").read()
    KAKAO_CLIENT_SECRET = open("./secret/kakao_client_secret.txt", "r").read()
    
    params = request.args.to_dict()
    code = params.get("code")
    
    callback_url = "http://127.0.0.1:8000/kakao/callback"    
    
    token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={KAKAO_CLIENT_ID}&client_secret={KAKAO_CLIENT_SECRET}&redirect_uri={callback_url}&code={code}")
    token_json = token_request.json()
    ACCESS_TOKEN = token_json.get("access_token")
    profile_request = requests.get(f"https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
    data = profile_request.json()
    
    return social_signin(data, "kakao")

@app.route('/whoami')
def whoami():
    user_id = session.get("user_id")
    user = User.query.filter_by(id=user_id).first()
    print(user)
    return f"<h1>{user}</h1>"

def social_signin(data, type):
    if type == "kakao":
        account_info = data.get("kakao_account")
        profile = account_info.get("profile")
        
        id = data.get("id")
        email = account_info.get("email")
        nickname = profile.get("nickname")
        profile_img = profile.get("profile_image_url"),
        created_at = datetime.datetime.now(),
        gender = account_info.get("gender"),
        login_type = LoginType.KAKAO
    
    elif type == "naver":
        account_info = data.get("response")
        
        id = account_info.get("id")
        email = account_info.get("email")
        nickname = account_info.get("nickname")
        profile_img = account_info.get("profile_image")
        created_at = datetime.datetime.now()
        gender = "male" if account_info.get("gender") == "M" else "female"
        login_type = LoginType.NAVER
    
    # 신규 유저 등록
    user = User.query.filter_by(id=id).first()
    if not user:
        new_user = User(
            id = id,
            email = email,
            nickname = nickname,
            profile_img = profile_img,
            created_at = created_at,
            gender = gender,
            login_type = login_type
        )
        db.session.add(new_user)
        db.session.commit()
    user_id = db.session.query(User.id).filter_by(email=email).first()[0]
    if user_id:
        session["user_id"] = user_id
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
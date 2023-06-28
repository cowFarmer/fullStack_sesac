from flask import Flask

# 플라스크 할당
app = Flask(__name__)

# 라우트 데코레이터
@app.route("/")
# 라우트 접속시 실행 함수
def home():
    return """summary line
    <h1>Hello Sesac</h1>
    <p>this is flask class</p>
    <ul>
    <li>1번</li>
    <li>2번</li>
    </ul>
    <body>
        <h1>hello im body</h1>
    </body>
    """

if __name__ == "__main__":
    app.run(debug=True, port=7000)
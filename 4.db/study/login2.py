import sqlite3

conn = sqlite3.connect("hello.db")

c = conn.cursor()

# 미션 1. 사용자 콘솔로부터 username, password를 받아 로그인하는 함수
def login(username, password):
    result = ""
    
    c.execute("SELECT username, password FROM users WHERE username=? AND password=?", (username, password))
    login_result = c.fetchall()
    
    if len(login_result) == 1:
        result = f"{username}님 로그인에 성공했습니다."
    else:
        result = "아이디와 비밀번호를 확인해주세요."
        
    return result

username = input("username: ")
password = input("password: ")
print(login(username, password))

conn.close()
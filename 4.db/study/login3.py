import sqlite3
import hashlib

conn = sqlite3.connect("hello.db")

c = conn.cursor()

# 미션2. 단방향 암호화 HASH를 사용해서 로그인 하는 코드 구현하기
def hash_password(password):
    hash_object = hashlib.sha256(password.encode()) # encode default 'utf-8'
    return hash_object.hexdigest()

def cleanup_table():
    c.execute('''DROP TABLE IF EXISTS users2''')
    c.execute('''CREATE TABLE users2
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT,
              password TEXT)''')
    conn.commit()

def insert_users():
    users = [
        ("user1", "abcd1111"),
        ("user2", "abcd2222"),
        ("user3", "abcd3333"),
        ("user4", "abcd4444"),
        ("user5", "abcd5555")
    ]
    
    for u in users:
        print(u)
        c.execute('''INSERT INTO users2(username, password) VALUES(?, ?)''', (u[0], hash_password(u[1])))
    conn.commit()

cleanup_table()
insert_users()


def login(username, password):
    result = ""
    password_hash = hash_password(password)
    
    c.execute('''SELECT username, password FROM users2 WHERE username = ? AND password = ?''', (username, password_hash))
    login_result = c.fetchall() # fetchall은 list로 return
    
    if len(login_result) == 1:
        result = f"{username}님 로그인에 성공했습니다."
    else:
        result = "아이디와 비밀번호를 확인해주세요."
        
    return result

username = input("username: ")
password = input("password: ")
print(login(username, password))

conn.close()
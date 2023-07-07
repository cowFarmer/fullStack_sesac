import sqlite3

# DB 접속
conn = sqlite3.connect("hello.db")

# conn을 통해 메시지를 주고 받음
# 로우레벨 접속한 소켓 인터페이스
# 커서 = 명령어를 주고 받는 위치 (ex: 마우스)
c = conn.cursor()

# 터미널에서 진행한 명령어 ''' 처리로 여러 줄도 가능
# c.execute("SELECT * FROM users")
c.execute("SELECT * FROM users")

# execute 결과 다 가져오기
users = c.fetchall()
# execute 결과 개수만큼 가져오기
# user = c.fetchone()
# user = c.fetchmany(10)

for user in users:
    print(user)

# 미션 로그인 로직
input_id = input("아이디를 입력해주세요: ")
input_pwd = input("비밀번호를 입력해주세요: ")

c.execute("SELECT username, password FROM users WHERE username=? AND password=?", (input_id, input_pwd))
result = c.fetchall()

if len(result) == 1:
    print(f"{input_id}님 로그인에 성공했습니다")
else:
    print("아이디와 비밀번호를 확인해주세요")

# commit은 DB 사용이 끝났을 때 변경 사항을 기록하기 위해 사용
conn.commit()

# 접속 종료
conn.close()
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('user.db')
cursor = conn.cursor()

# 사용자 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT)''')

# 몇 명의 사용자 추가
users = [
    ('John Doe', 25, 'Male'),
    ('Jane Smith', 30, 'Female'),
    ('Michael Johnson', 35, 'Male'),
    ('Emily Davis', 28, 'Female'),
    ('David Lee', 32, 'Male'),
    ('Emma Wilson', 27, 'Female'),
    ('Daniel Brown', 31, 'Male'),
    ('Olivia Taylor', 29, 'Female'),
    ('Sophia Anderson', 33, 'Female'),
    ('Matthew Martin', 26, 'Male')
]

# cursor.executemany('INSERT INTO users (name, age, gender) VALUES (?, ?, ?)', users)

# 변경사항 저장
conn.commit()

# 미션 1. 성별이 여자인 사람만 출력하기
cursor.execute('''
               SELECT * FROM users WHERE gender = "Female";
               ''')
result = cursor.fetchall()
print("# 미션 1. 성별이 여자인 사람만 출력하기")
print(result)
print("-"*20)

# 미션 2. 나이가 30살 이상인 사람만 출력하기
cursor.execute('''
               SELECT * FROM users WHERE age >= 30;
               ''')
result = cursor.fetchall()
print("# 미션 2. 나이가 30살 이상인 사람만 출력하기")
print(result)
print("-"*20)

# 미션 3. 나이가 25살 이상 30살 이하인 사용자 출력하기
cursor.execute('''
               SELECT * FROM users WHERE age >= 25 AND age <= 30;
               ''')
result = cursor.fetchall()
print("# 미션 3. 나이가 25살 이상 30살 이하인 사용자 출력하기")
print(result)
print("-"*20)

# 미션 4. 성별로 그룹핑 몇 명인지 출력하기
cursor.execute('''
               SELECT gender, COUNT(*) FROM users GROUP BY gender;
               ''')
result = cursor.fetchall()
print("# 미션 4. 성별로 그룹핑 몇 명인지 출력하기")
print(result)
print("-"*20)


# 미션 5. John Doe의 나이를 26살로 업데이트 하기
cursor.execute('''
               UPDATE users SET age = age + 1 WHERE name = "John Doe";
               ''')
# conn.commit()

cursor.execute('''
               SELECT * FROM users WHERE name = "John Doe";
               ''')
result = cursor.fetchall()
print("# 미션 5. John Doe의 나이를 26살로 업데이트 하기")
print(result)
print("-"*20)

# 미션 6. Emily Davis 사용자를 삭제하기
cursor.execute('''
               DELETE FROM users WHERE name = "Emily Davis";
               ''')
# conn.commit()

cursor.execute('''
               SELECT * FROM users
               ''')

result = cursor.fetchall()
print("# 미션 6. Emily Davis 사용자를 삭제하기")
print(result)
print("-"*20)

conn.close()
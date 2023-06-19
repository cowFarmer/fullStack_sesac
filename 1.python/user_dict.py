users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]

# 이름을 입력 받아 사용자 정보를 반납하기
# 1. 이름을 입력 받아서 반납하기
def find_users(name):
    result = []
    for user in users:
        if user['name'] == name:
            result.append(user)
    return result

print(find_users('Bob'))

# 2. 이름과 나이를 입력 받아서 반납하기
def find_users_two(name, age):
    result = []
    for user in users:
        if user['name'] == name and user['age'] == age:
            result.append(user)
    return result

print(find_users_two('Bob', 30))

# 3. 인자 값이 여러 개인 경우 어떻게 해야 할까?
search_user = {
    "name": "Bob",
    "age": 30,
}

def find_users_three(search_user):
    result = []
    for user in users:
        if user['name'] == search_user['name'] and user['age'] == search_user['age']:
            result.append(user)
    return result

result = find_users_three(search_user)
print(result)
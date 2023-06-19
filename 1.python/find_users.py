# find_users(search_user): 함수를 완성하시오.

# search_user = { } 안에 있는 조건이 모두 매칭하는 사용자를 찾아내시오.
# 예). {"name" : "Bob" } 이 있으면 이름으로만 검색하고, {"name" : "Bob", "age" : 30} 이 있으면 이 두가지를 AND 로 비교해서 검색하고... 등

users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]

search_user = {
    "name": "Bob",
    "age": 30,
}

def find_users(**info):
    check = []
    for user in users:
        cnt = 0
        user_key_list = list(user.keys())
        user_value_list = list(user.values())
        info_key_list = list(info.keys())
        info_value_list = list(info.values())
        
        for i in range(len(info_key_list)):
            if info_key_list[i] in user_key_list[user_key_list.index(info_key_list[i])]:
                if info_value_list[i] == user_value_list[user_key_list.index(info_key_list[i])]:
                    cnt += 1
                    print(info_value_list[i], user_value_list[user_key_list.index(info_key_list[i])])
        if cnt == len(info_key_list):
            check.append(user)
    return check

print(find_users(**search_user))
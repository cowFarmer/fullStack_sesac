# # find_users(search_user): 함수를 완성하시오.

# # search_user = { } 안에 있는 조건이 모두 매칭하는 사용자를 찾아내시오.
# # 예). {"name" : "Bob" } 이 있으면 이름으로만 검색하고, {"name" : "Bob", "age" : 30} 이 있으면 이 두가지를 AND 로 비교해서 검색하고... 등

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
    info_key_list = list(info.keys())
    info_value_list = list(info.values())
    
    for user in users:
        cnt = 0
        user_key_list = list(user.keys())
        user_value_list = list(user.values())
        
        
        for i in range(len(info_key_list)):
            if info_key_list[i] in user_key_list[user_key_list.index(info_key_list[i])]:
                if info_value_list[i] == user_value_list[user_key_list.index(info_key_list[i])]:
                    cnt += 1
        if cnt == len(info_key_list):
            check.append(user)
    return check

print(find_users(**search_user))

################################
# v1
def find_users(search_user):
    result = []
    for user in users:
        if (search_user.get("name") is None or search_user.get("name") == user.get("name") and\
            (search_user.get("age") is None or search_user.get("age") == user.get("age")) and\
            (search_user.get("location") is None or search_user.get("location") == user.get("location"))):
            result.append(user)
        return result
    
# v2
def matches_criteria(user, condition):
    for key, value in condition.items():
        if user.get(key) != value:
            return False
    return True


def find_users(search_user):
    result = []
    for user in users:
        if matches_criteria(user, search_user):
            result.append(user)
    return result

search_bob1 = {"name": "Bob"} # 1
search_bob2 = {"name": "Bob", "age": 30} # 1
search_bob3 = {"name": "Alice", "age": 35} # 0
search_bob4 = { } # 3
search_bob5 = {"location": "Busan", "age": 30} # 1


# 유닛테스트 v1
def test_find_users():
    result = True
    if len(find_users(search_bob1)) != 1:
        result = False
    if len(find_users(search_bob2)) != 1:
        result = False
    if len(find_users(search_bob3)) != 0:
        result = False
    if len(find_users(search_bob4)) != 3:
        result = False
    if len(find_users(search_bob5)) != 1:
        result = False
        
    if result:
        print("PASS")
    else:
        print("FAIL")

test_find_users()

# 유닛테스트 v2
def test_find_users2():
    search_box = [search_bob1, search_bob2, search_bob3, search_bob4, search_bob5]
    result_box = [1,1,0,3,1]
    final_result = True
    
    for search_case in search_box:
        if len(find_users(search_case)) != result_box[search_box.index(search_case)]:
            final_result = False
            
    if final_result:
        print("PASS")
    else:
        print("FAIL")
test_find_users2()

# 유닛테스트 v3
test_cases = [
        {"case": search_bob1, "expected_result": 1},
        {"case": search_bob2, "expected_result": 1},
        {"case": search_bob3, "expected_result": 0},
        {"case": search_bob4, "expected_result": 3},
        {"case": search_bob5, "expected_result": 1}
    ]

def test_find_users3():
    final_result = True
    for test_case in test_cases:
        if len(find_users(test_case["case"])) != test_case["expected_result"]:
            final_result = False
            
    if final_result:
        print("PASS")
    else:
        print("FAIL")
test_find_users3()
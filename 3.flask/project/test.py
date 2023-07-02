# test_dict = {"age_group": 10}
# info_dict = {'id': '06dcbb0c-68db-420d-9218-9519ef908e44', 'name': '박성민', 'gender': 'male', 'age': '16', 'birthdate': '2006-06-15', 'address': '서울 강서구 43길 77'}

# if "age_group" in test_dict:
#     tmp_num = test_dict.get("age_group")
#     test_dict = {"age_group": [_ for _ in range(tmp_num, tmp_num+10)]}

# for key, value in test_dict.items():
#     print(info_dict.get("age"))
#     print(test_dict.get(key))
#     if info_dict.get("age") in test_dict.get(key):
#         print(info_dict)

# if all(info_dict.get(key) in value for key, value in test_dict.items()):
#     print(info_dict)

age = 16
age_group = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

if age in age_group:
    print(age)
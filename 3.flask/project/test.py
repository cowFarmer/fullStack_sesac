import csv
# tmp_dict = [
#     {'Id': '556ab94a-e782-49f0-a23c-55251ff06b88', 'Name': '임예지', 'Gender': 'Male', 'Age': '31', 'Birthdate': '1992-05-24', 'Address': '대구 강서구 81길 64'},
#     {'Id': '934bfac0-ed07-48ce-89ff-bfec277e77eb', 'Name': '강지안', 'Gender': 'Female', 'Age': '40', 'Birthdate': '1983-04-08', 'Address': '대구 강서구 21길 26'},
#     {'Id': '3b4514bb-48b4-41ca-b6ad-0cf514910c3d', 'Name': '민현우', 'Gender': 'Female', 'Age': '30', 'Birthdate': '1992-09-17', 'Address': '광주 중구 21로 96'},
#     {'Id': '3b4514bb-48b4-41ca-b6ad-0cf514910c3d', 'Name': '윤민우', 'Gender': 'male', 'Age': '30', 'Birthdate': '1992-09-17', 'Address': '광주 중구 21로 96'},
# ]

# filter_dict = {"Gender": "Female"}

# for line in tmp_dict:
#     print(line["Name"])
#     if all(line.get(key) == value for key, value in filter_dict.items()):
#         print(line)

user_csv_file = "./csv/user.csv"

with open(user_csv_file, "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        
        for line in lines:
            lines_lower = {key.lower(): value for key, value in lines.items()}
            
        print(lines_lower)
        # for line in lines_lower:
        #     print(line)
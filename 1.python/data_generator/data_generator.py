import random
import os
import csv

names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
gender_type = ['male', 'female']

# 성, 이름
last_names = []
first_names = []

# class GeneratorHuman:
#     def __init__(self, make_number, result_type, cities_file, names_file):
#         self.make_number = make_number
#         self.result_type = result_type
#         self.cities_file = cities_file
#         self.names_file = names_file
    
        



def generate_name():
    return random.choice(names)

def generate_name_kor():
    return random.choice(last_names)+random.choice(first_names)

def generate_birthday():
    mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = random.randint(1980,2013)
    month = random.randint(1,12)
    # leap year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        mdays[2] = 29
    day = random.randint(1, mdays[month])
    return f"{year}-{month}-{day}"

def generate_gender():
    return random.choice(gender_type)

def generate_cities():
    return f"{random.randint(1,100)} {random.choice(cities)}"

def generate_cities_kor():
    korea_areas = ["서울", "경기", "강원", "충청북도", "충청남도", "경상북도", "경상남도", "전라북도", "전라남도", "제주"]
    seoul_areas = ["강남구", "강동구", "강서구", "강북구", "관악구", "광진구", "구로구", "금천구", "노원구", "동대문구", "도봉구", "동작구", "마포구", "서대문구", "성동구", "성북구", "서초구", "송파구", "영등포구", "용산구", "양천구", "은평구", "종로구", "중구", "중랑구"]
    road_names = ["로", "길", "대로", "번길"]
    return f"{random.choice(korea_areas)} {random.choice(seoul_areas)} {random.randint(1, 100)}{random.choice(road_names)} {random.randint(1, 100)}"

def sum_human_info(count, data_list):
    for _ in range(count):
        name = generate_name_kor()
        birthday = generate_birthday()
        gender = generate_gender()
        city = generate_cities_kor()
        
        data_list.append(f"{name},{birthday},{gender},{city}")

# txt 파일 읽고 배열에 넣어주기
def read_file(filename, append_list):
    current_dir = os.getcwd()
    file = open(current_dir + "/" + filename + ".txt", "r")
    while True:
        line = file.readline()
        if not line:
            break    
        append_list.append(line.strip())
    return sorted(list(set(append_list)))

# csv 파일 없으면 만들고 쓰기 csv 파일이 있다면 덮어쓰기이니 주의할것!!!!!
def write_data_to_csv(filename):
    current_dir = os.getcwd()
    file_pwd = current_dir + "/" + filename + ".csv"
    if os.path.isfile(file_pwd) == False:
        open(file_pwd, "w").close()
    if len(datas) <= 1:
        return "data list에 data가 없습니다. 데이터를 만들어주세요."
    else:
        file = open(file_pwd, "w")
        for line in datas:
            data_writer = csv.writer(file)
            data_writer.writerow([line])
        file.close()

# result type 선택하기
def result_type(csv_or_console):
    if csv_or_console == "csv":
        write_data_to_csv('test')
    elif csv_or_console == "console":
        for data in datas:
            print(data)
    else:
        print("csv or console 둘 중 하나만 지원합니다.")

make_number = int(input("생성할 데이터 개수를 입력하세요.\n"))
datas = ["Name,Birthday,Gender,Address"]

# 영문용
# read_file('cities', cities)
# read_file('names', names)

# 한글용
read_file('last_names', last_names)
read_file('first_names', first_names)
sum_human_info(make_number, datas)


        
result_csv_or_console = input("결과물 출력을 위해 하나만 입력해주세요. 'csv' or 'console'\n").lower()
result_type(result_csv_or_console)

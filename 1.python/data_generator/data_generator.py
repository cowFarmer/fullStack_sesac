import random
import os
import csv

names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
gender_type = ['male', 'female']

def generate_name():
    return random.choice(names)

def generate_birthday():
    mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = random.randint(1980,2023)
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

def sum_human_info(count, data_list):
    for _ in range(count):
        name = generate_name()
        birthday = generate_birthday()
        gender = generate_gender()
        city = generate_cities()
        
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

read_file('cities', cities)
read_file('names', names)
sum_human_info(make_number, datas)


        
result_csv_or_console = input("결과물 출력을 위해 하나만 입력해주세요. 'csv' or 'console'\n").lower()
result_type(result_csv_or_console)

import random
import os
import csv
import datetime

# 데이터 만들기 
### 나중에 모드 추가할 예정
class PersonDataGenerator:
    def __init__(self):
        # 참조할 name이 있는지 확인
        self.name = GenerateName().get_name()
        self.birthday = GenerateBirthday().get_birthday()
        self.age = GenerateAge().get_age()
        self.gender = GenerateGender().get_gender()
        self.address = GenerateAddress().get_address()
        self.person_data = f"{self.name}, {self.birthday}, {self.age}, {self.gender}, {self.address}"
    
    ### 카운트 추가하기
    def get_person_data(self):
        return self.person_data

# 이름 만들기
### 파일 읽은 후 name 작업 추가 필요
class GenerateName:
    def __init__(self):
        self.last_names = ["test1", "tst2", "tset3"]
        self.first_names = ["현호", "혀후", "하후", "히후"]
        self.name = random.choice(self.last_names)+random.choice(self.first_names)
    
    def get_name(self):
        return self.name
    
# 생일 만들기    
class GenerateBirthday:
    def __init__(self):
        self.mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.year = random.randint(1980,2013)
        self.month = random.randint(1,12)
        # leap year
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
            self.mdays[2] = 29
        self.day = random.randint(1, self.mdays[self.month])
        self.birthday = f"{self.year}-{self.month:02d}-{self.day:02d}"
        
    def get_birthday(self):
        return self.birthday
    
# 나이 만들기
class GenerateAge(GenerateBirthday):
    def __init__(self):
        super().__init__()
        self.today = str(datetime.datetime.now()).split(' ')[0]
        self.birthday = ''.join(self.birthday.split('-'))
        self.today = ''.join(self.today.split('-'))
    
        # 금일 날짜 기준 나이 구하기
        self.birthday_year, self.birthday_md = int(self.birthday[:4]), int(self.birthday[4:])
        self.today_year, self.today_md = int(self.today[:4]), int(self.today[4:])
        self.age = self.today_year - self.birthday_year
        if self.today_md < self.birthday_md:
            self.age -= 1
        
    def get_age(self):
        return self.age
    
# 성별 만들기
class GenerateGender:
    def __init__(self):
        self.gender = random.choice(["male", "female"])
        
    def get_gender(self):
        return self.gender

# 지역 만들기
class GenerateAddress:
    def __init__(self):
        self.korea_areas = ["서울", "경기", "강원", "충청북도", "충청남도", "경상북도", "경상남도", "전라북도", "전라남도", "제주"]
        self.seoul_areas = ["강남구", "강동구", "강서구", "강북구", "관악구", "광진구", "구로구", "금천구", "노원구", "동대문구", "도봉구", "동작구", "마포구", "서대문구", "성동구", "성북구", "서초구", "송파구", "영등포구", "용산구", "양천구", "은평구", "종로구", "중구", "중랑구"]
        self.road_names = ["로", "길", "대로", "번길"]
        self.address = f"{random.choice(self.korea_areas)} {random.choice(self.seoul_areas)} {random.randint(1, 100)}{random.choice(self.road_names)} {random.randint(1, 100)}"
    
    def get_address(self):
            return self.address

# 파일 읽기
class ReadFile:
    def __init__(self, filename, append_list):
        self.filename = filename
        self.append_list = []
        # self.append_list = append_list
    
    def read(self):
        with open("./src/" + self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.append_list.append(line.strip())
        file.close()
        return list(set(self.append_list))
    
# 파일 쓰기
class WriteFile:
    def __init__(self, filename, datas):
        self.filename = filename
        self.datas = datas
    
    def write(self):
        with open("./src/" + self.filename, "w", newline="\n") as file:
            csv_file = csv.writer(file)
            for line in self.datas:
                csv_file.writerow(line)
            file.close()

if __name__ == "__main__":
    generate_person_info = PersonDataGenerator()
    person_info = generate_person_info.get_person_data()
    print(person_info)
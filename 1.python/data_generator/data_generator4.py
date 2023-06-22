### 사용자 코드와 상점 코드 합치기
import random
import csv
import datetime

# 이름 만들기
class GenerateName:
    def __init__(self):
        self.last_names = []
        self.first_names = []
        
        # 참조하는 txt 파일 읽기
        self.last_names = ReadFile("last_names.txt", self.last_names).read()
        self.first_names = ReadFile("first_names.txt", self.first_names).read()
    
    def get_name(self):
        return random.choice(self.last_names)+random.choice(self.first_names)

# 생일 만들기
class GenerateBirthday:
    def __init__(self):
        self.mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    def get_birthday(self):
        self.year = random.randint(1980,2013)
        self.month = random.randint(1,12)
        # leap year
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
            self.mdays[2] = 29
        self.day = random.randint(1, self.mdays[self.month])
        self.birthday = f"{self.year}-{self.month:02d}-{self.day:02d}"
        return self.birthday

# 나이 만들기
class GenerateAge():
    def __init__(self, birthday):
        self.today = str(datetime.datetime.now()).split(" ")[0]
        self.birthday = birthday
        self.birthday = "".join(self.birthday.split("-"))
        self.today = "".join(self.today.split("-"))
    
        # 만 나이 구하기
        self.birthday_year, self.birthday_md = int(self.birthday[:4]), int(self.birthday[4:])
        self.today_year, self.today_md = int(self.today[:4]), int(self.today[4:])
        self.age = self.today_year - self.birthday_year
        if self.today_md < self.birthday_md:
            self.age -= 1
        
    def get_age(self):
        return self.age

# 성별 만들기
class GenerateGender:
    def get_gender(self):
        return random.choice(["male", "female"])

# 지역 만들기
class GenerateAddress:
    def __init__(self):
        self.korea_areas = ["서울", "경기", "강원", "충청북도", "충청남도", "경상북도", "경상남도", "전라북도", "전라남도", "제주"]
        self.seoul_areas = ["강남구", "강동구", "강서구", "강북구", "관악구", "광진구", "구로구", "금천구", "노원구", \
                            "동대문구", "도봉구", "동작구", "마포구", "서대문구", "성동구", "성북구", "서초구", "송파구", \
                            "영등포구", "용산구", "양천구", "은평구", "종로구", "중구", "중랑구"]
        self.road_names = ["로", "길", "대로", "번길"]
    
    def get_address(self):
        self.address = f"{random.choice(self.korea_areas)} {random.choice(self.seoul_areas)} {random.randint(1, 100)}{random.choice(self.road_names)} {random.randint(1, 100)}"
        return self.address
    
# 상점 종류 만들기
class GenerateStore:
    def __init__(self):
        self.store_list = ["스타벅스", "투썸플레이스", "메가커피", "이디야", "빽다방", "컴포즈커피", "커피에반하다", "요거프레소", "커피베이", "할리스", "엔제리너스"]
    
    def get_name(self):
        self.name = random.choice(self.store_list)
        return self.name
    
# 상점 이름 만들기
class GenerateStoreName:
    def __init__(self, store):
        self.store = store
    
    def get_type(self):
        return f"{self.store} {random.randint(1,15)}호점"
    
# 만든 데이터 합치기
class GeneratorData:
    def __init__(self):
        self.gen_name = GenerateName()
        self.gen_birthday = GenerateBirthday()
        self.gen_gender = GenerateGender()
        self.gen_address = GenerateAddress()
        self.gen_store_name = GenerateStore()
        
    def generate_data(self, count, category):
        datas = []
        for _ in range(count):
            address = self.gen_address.get_address()
            if category == "user":
                name = self.gen_name.get_name()
                birthday = self.gen_birthday.get_birthday()
                age = GenerateAge(birthday).get_age()
                gender = self.gen_gender.get_gender()
                datas.append([name, gender, age, birthday, address])
            if category == "store":
                store_name = self.gen_store_name.get_name()
                store_type = GenerateStoreName(store_name).get_type()
                datas.append([store_name, store_type, address])
        return datas
    
    def category_header_file_name(self, category):
        user_file_name = "person_data.csv"
        cafe_file_name = "cafe_data.csv"
        
        if category == "user":
            return ["Name", "Gender", "Age", "Birthday", "Address"], user_file_name
        elif category == "store":
            return ["Name", "Type", "Address"], cafe_file_name

# 파일 읽기
class ReadFile:
    def __init__(self, filename, append_list):
        self.filename = filename
        self.append_list = append_list
    
    def read(self):
        with open("./src/" + self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                self.append_list.append(line.strip())
        file.close()
        return list(set(self.append_list))
                        
# 사람 파일 출력하기
class PrinterData(GeneratorData):
    def print_data(self, count, category):
        datas = self.generate_data(count, category)
        header, save_file_name = self.category_header_file_name(category)
        
        print(header)
        for data in datas:
            print(data)

# 파일 쓰기
class WriterData(GeneratorData):
    def write_data(self, count, category):
        datas = self.generate_data(count, category)
        header, save_file_name = self.category_header_file_name(category)

        with open("./src/" + save_file_name, "w", newline="\n") as file:
            csv_file = csv.writer(file)
            csv_file.writerow(header)
            for line in datas:
                csv_file.writerow(line)
            file.close()

# Input 받아서 검증 후 반환하는 클래스
class CheckerInputType:
    # 데이터 유형
    def category_list(self):
        category_list = ["user", "store", "item"]
        while True:
            data_category = input("데이터 유형을 입력하세요 'User', 'Store' or 'Item': ")
            if data_category.lower() in category_list:
                data_category = data_category.lower()
                break
            else:
                print("데이터 유형을 알맞게 입력하세요 'User', 'Store' or 'Item': ")
        return data_category
    
    # 데이터 개수
    def count_generate_items(self):
        while True:
            try:
                count_generate_items = abs(int(input("생성할 데이터 개수를 입력하세요: ")))
                break
            except ValueError:
                print("생성할 데이터 개수를 숫자로 입력하세요: ")
        return count_generate_items
    
    # 데이터 아웃풋 타입
    def input_type(self):
        input_type_list = ["console", "csv"]
        while True:
            input_type = input("출력 타입을 입력하세요 'console', 'csv': ")
            if input_type.lower() in input_type_list:
                break
            else:
                print("출력 타입을 알맞게 입력하세요 'console', 'csv': ")
        return input_type
    
if __name__ == "__main__":
    checker = CheckerInputType()
    data_category = checker.category_list()
    count_generate_items = checker.count_generate_items()
    input_type = checker.input_type()
    writer = WriterData()
    printer = PrinterData()
    
    if input_type == "console":
        printer.print_data(count_generate_items, data_category)
    elif input_type == "csv":
        writer.write_data(count_generate_items, data_category)
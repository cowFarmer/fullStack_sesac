import datetime

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
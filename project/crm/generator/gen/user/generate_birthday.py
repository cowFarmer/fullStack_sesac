import random

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
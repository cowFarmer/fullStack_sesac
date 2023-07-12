import random
import datetime


class GenerateOrderAt:
    def __init__(self):
        self.mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.year = random.randint(2022,2023)
        self.month = random.randint(1,12)
        
    def get_order_at(self):
        # leap year
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
            self.mdays[2] = 29
        self.day = random.randint(1, self.mdays[self.month])
        hour = random.randint(1,24)
        minute = random.randint(1,60)
        second = random.randint(1,60)
        self.order_at = datetime.datetime(self.year, self.month, self.day, hour, minute, second)
        return self.order_at
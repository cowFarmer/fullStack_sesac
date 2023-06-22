import random

class GenerateStore:
    def __init__(self):
        self.store_list = ["스타벅스", "투썸플레이스", "메가커피", "이디야", "빽다방", "컴포즈커피", "커피에반하다", "요거프레소", "커피베이", "할리스", "엔제리너스"]
    
    def get_name(self):
        self.name = random.choice(self.store_list)
        return self.name
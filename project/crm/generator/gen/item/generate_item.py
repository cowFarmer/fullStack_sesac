import random

class GenerateItemInfo:
    def __init__(self):
        self.items = [
            ["아메리카노", "커피", "3000"],
            ["카페라떼", "커피", "3500"],
            ["카페모카", "커피", "4000"],
            ["아포카토", "커피", "4000"],
            ["카푸치노", "커피", "4000"],
            ["카라멜마끼아또", "커피", "4000"],
            ["그린티", "티", "3500"],
            ["허브티", "티", "3500"],
            ["밀크티", "티", "4000"],
            ["아이스티", "티", "3500"],
            ["케이크", "디저트", "5000"],
            ["티라미수", "디저트", "5000"],
            ["마카롱", "디저트", "3000"],
            ["베이글", "디저트", "4000"],
            ["머핀", "디저트", "4000"],
            ["허니 브레드", "디저트", "4000"],
        ]

    def get_item_name(self):
        self.item = random.choice(self.items)
        return self.item[0]
    
    def get_item_type(self, name):
        for i in range(len(self.items)):
            if self.items[i][0] == name:
                index = i
                break
        self.item_type = self.items[index][1]
        return self.item_type
    
    def get_item_price(self, name):
        for i in range(len(self.items)):
            if self.items[i][0] == name:
                index = i
                break
        self.item_price = self.items[index][2]
        return self.item_price
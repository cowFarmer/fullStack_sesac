import random

class GenerateItemInfo:
    def __init__(self):
        self.items = [
            ["아메리카노", "커피", "3000"],
            ["에스프레소", "커피", "4000"],
            ["카페라떼", "커피", "3500"],
            ["카페모카", "커피", "4000"],
            ["화이트 초콜릿 모카", "커피", "5900"],
            ["토피 넛 라떼", "커피", "6100"],
            ["아포카토", "커피", "4000"],
            ["카푸치노", "커피", "4000"],
            ["카라멜 마끼아또", "커피", "4000"],
            ["콜드 브루", "커피", "4900"],
            ["바닐라 크림 콜드 브루", "커피", "5800"],
            ["모카 프라푸치노", "커피", "5900"],
            ["그린 티", "티", "3500"],
            ["허브 티", "티", "3500"],
            ["밀크 티", "티", "4000"],
            ["아이스 티", "티", "3500"],
            ["민트 티", "티", "5900"],
            ["유자 민트 티", "티", "5900"],
            ["자몽 허니 블랙 티", "티", "5700"],
            ["케이크", "디저트", "5000"],
            ["티라미수", "디저트", "5000"],
            ["티라미수 롤", "디저트", "6500"],
            ["마카롱", "디저트", "3000"],
            ["베이글", "디저트", "4000"],
            ["머핀", "디저트", "4000"],
            ["허니 브레드", "디저트", "4000"],
            ["라즈베리 쇼콜라", "디저트", "5900"],
            ["레드벨벳 크림치즈 케이크", "디저트", "6500"],
            ["에크 타르트", "디저트", "4500"],
            ["생크림 케이크", "디저트", "6600"]
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
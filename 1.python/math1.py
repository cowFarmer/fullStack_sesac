import math

# 원의 넓이 구하기
radius = 5
area = math.pow(radius,2) * math.pi
print(area)

# 랜덤 넘버 다이스 만들기
import random

def roll_dice():
    dice_roll = random.randint(1, 6)
    print(dice_roll)

for _ in range(10):
    roll_dice()

# 랜덤 셔플하기
my_list = [1,2,3,4,5]
def shuffle(input_list):
    random.shuffle(input_list)
    return my_list

print(shuffle(my_list))
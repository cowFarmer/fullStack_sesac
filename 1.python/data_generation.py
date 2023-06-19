import random

name = ['Jane', 'Emily', 'Olivia', 'Michael']
address = ['New York', 'Philadelphia', 'Los Angeles', 'Chicago', 'Huston']

def dataGeneration(number):
    for i in range(number):
        print(random.randint(1900,2023))
        print(random.randint(1,12))
        print(random.randint(1,31))
        print(random.randint(0, 1))
        print(random.randint(0,len(name)-1))
        
    
make_num = int(input('생성할 데이터 개수를 입력하세요. \n'))
dataGeneration(make_num)
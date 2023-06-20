import calendar

def print_calendar(year, month):
    print(calendar.month(year, month))

print_calendar(2023, 6)

def make_calendar(year, month):
    # 0년 1월 1일은 일요일
    # 500년 1월 1일은 금요일
    
    first_day = ((year * 365) + (year // 4) - year // 100 + year // 400) % 7
    mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['일', '월', '화', '수', '목', '금', '토']
    
    # 윤년
    if year % 4 == 0 and (year % 100 == 0 and year % 400 == 0):
        mdays[2] = 29
        
    for i in range(1, month):
        first_day += mdays[i]
    
    first_day = first_day % 7
    # print(first_day)
    print(f'     {month}월 {year}년')
    print(' '.join(day))
    
    
    dday_list = []
    
    for _ in range(1, first_day+1):
        print(end='   ')    
    for i in range(1, mdays[month]+1):
        if (i+first_day-1) % 7 == 0:
            print('\n')
        if i / 10 < 1:
            print(i, ' ', end='')
        else:
            print(i, end=' ')
    
make_calendar(2023, 6)
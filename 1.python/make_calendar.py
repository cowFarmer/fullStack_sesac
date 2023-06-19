# import calendar

# def print_calendar(year, month):
#     print(calendar.month(year, month))

# print_calendar(2023, 6)

def make_calendar(year, month):
    first_day = year * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    day = ['일', '월', '화', '수', '목', '금', '토']
    print(f'{month}월 {year}년')
    print('  '.join(day))
    print(first_day)
    
make_calendar(0, 1)
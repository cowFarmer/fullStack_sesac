numbers = [1,2,3,4,5]

def get_number(index):
    try:
        # 오류 가능성이 있는 코드 블럭
        return numbers[index]
    except IndexError:
        # index 오류 처리 방법
        return "input의 index 값이 잘못 되었습니다."
    except TypeError:
        # type 오류 처리 방법
        return "input type이 잘못 되었습니다."

print(get_number(-10))
print(get_number(5))
print(get_number(0))
print(get_number(-1))
print(get_number('a'))
print("-"*10)

# 1. 글자를 입력 받아 숫자로 변환하여 반환하기
def convert_to_integer(string):
    value = None
    try:
        value = int(string)
    except ValueError:
        return "input 값이 잘못 되었습니다."
    
    return value, type(value)
    
print(convert_to_integer("10"))
print(convert_to_integer("5"))
print(convert_to_integer("-5"))
print(convert_to_integer("A"))
print(convert_to_integer("Hello"))

# 2. 사용자로부터 입력 받는 기능 추가하기
def convert_to_integer_input(string):
    value = None
    try:
        value = int(string)
    except ValueError:
        return "input 값이 잘못 되었습니다."
    
    return value, type(value)
    
print(convert_to_integer_input(input('값을 입력하세요.\n')))
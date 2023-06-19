# 사용자로부터 문자(문장)을 받아 대, 소문자 바꿔서 변환하기.
def convert_case(text):
    result = ''
    for c in text:
        if c.islower():
            result += c.upper()
        elif c.isupper():
            result += c.lower()
        else:
            result += c
    return result

text = input('문장을 입력하세요\n')
result = convert_case(text)
print(result)
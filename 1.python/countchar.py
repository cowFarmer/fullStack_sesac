# 1. 원하는 글자 세기
sentence = "Hello, world!"

def count_char(char):
    return sentence.count(char)

char = 'o'
count = count_char(char)
print(f"글자 {char}, 개수: {count}")

def count_char2(input_char):
    count = 0
    for char in sentence:
        if char == input_char:
            count += 1
    return count

char = 'l'
count = count_char2(char)
print(f"글자 {char}, 개수: {count}")

# 2. 대소문자 구분 없이 글자 세기
def count_char3(input_char):
    count = 0
    for char in sentence:
        if input_char.lower() == char.lower():
            count += 1
    return count

char = 'h'
count = count_char3(char)
print(f"글자 {char}, 개수: {count}")

# 리스트 컴프리헨션, list comprehension
# 1 ~ 10까지 각 숫자의 제곱으로 이루어진 목록을 만들 때
squares = [x ** 2 for x in range(1, 11) if x > 5]

print(squares)

# 1 ~ 20 짝수들 리스트 생성하기
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)
evens = [x*2 for x in range(1, 11)]
print(evens)

# 문자열의 각 글자를 순회하면서 대문자로 바꾸시오
word = 'hello'
upper_letters = []
upper_letters = [word.upper()]
upper_letters2 = [c.upper() for c in word]
print(upper_letters)
print(upper_letters2)

# 문자열 길이가 3 이하인 단어들만 선택하기
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'egg']
short_words = []
for word in words:
    if len(word) <= 3:
        short_words.append(word)
print(short_words)

short_words = []
short_world = [short_words.append(word) for word in words if len(word) <= 3]
print(short_words)
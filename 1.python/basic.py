# tuple (a, b)
def get_name_and_age():
    return 'noah', 98

if __name__ == '__main__':
    name, age = get_name_and_age()
    print(name)
    print(age)
    
# list []
shopping_list = ['apple', 'banana', 'orange']
shopping_list.append('grape')
print(shopping_list)
shopping_list.remove('banana')
print(shopping_list)

for product in shopping_list:
    if product == 'apple':
        continue
    print(product)

# dictionary
# key-value, ex) 'name': '노현호'
student = {
    "name": "noah",
    "age": 98,
    "university": "ABC uni"
}

print(student)
print(student['name'])
print("age:", student['age'])

# -------------------------------------------------
# 홀수 리스트와 짝수 리스트를 따로 만들어서 목록에 추가하기
even_numbers = []
odd_numbers = []

for i in range(1, 11):
    if i % 2 == 0:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)
        
print('홀수')
print(even_numbers)
print('짝수')
print(odd_numbers)

# 학생 grade 만들기
student_grades = {'A': 85, 'B': 92, 'C': 78, 'D': 95}

# 90점 이상인 학생을 출력하시오
for i in student_grades:
    if student_grades[i] >= 90:
        print(f'90점 이상인 학생은 {i} 입니다.')
        
# case2
for student, grade in student_grades.items():
    print(student, grade)


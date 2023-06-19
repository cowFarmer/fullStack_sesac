numbers = [1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 6, 5]

# 입력 받은 값에서 중복을 제거하기
def remove_duplicate(numbers):
    unique_list = []
    [unique_list.append(num) for num in numbers if num not in unique_list]
    # for num in numbers:
    #     if num not in unique_list:
    #         unique_list.append(num)
    return unique_list

print(f"원본 리스트: {numbers}")
print(f"유닉 리스트: {remove_duplicate(numbers)}")
print("-"*10)

# set 이용하기
def remove_duplicate2(numbers):
    return sorted(list(set(numbers)))
print(f"원본 리스트2: {numbers}")
print(f"유닉 리스트2: {remove_duplicate2(numbers)}")
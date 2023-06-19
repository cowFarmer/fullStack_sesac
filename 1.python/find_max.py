numbers = [3, 2, 1, 7, 9, 10]
# numbers = [-1, -123, -50, -19, -6, -213894]

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if max < number:
            max = number
    return max
print(find_max(numbers))

def find_max_two(numbers):
    numbers = sorted(numbers)
    return numbers[-1]
print(find_max_two(numbers))

def find_max_three(number_list):
    return max(number_list)

number_list = list(map(int, input().split()))
print(find_max_three(number_list))
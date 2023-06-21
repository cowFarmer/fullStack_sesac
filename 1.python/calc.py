# 계산기 만들기
# 사용자로부터 입력을 받아서 계산을 한다
# 연산 모드를 입력 받는다: 덧셈, 뺄셈, 곱셈, 나눗셈
# 숫자를 2개 입력 받는다
# return 실행 예시
# plus / minus / multiply / division

def mode_option():
    mode_ops = ["plus", "minus", "multiply", "division", "quit"]
    calc_mode = input(f"연산 모드를 입력하세요: {mode_ops}\n")
    if calc_mode not in mode_ops:
        print("연산 모드를 인식하지 못했습니다.")
        calc_mode = mode_option()
    return calc_mode

def input_value1():
    try:
        val1 = int(input("숫자1\n"))
        return val1
    except ValueError:
        print("숫자가 입력되지 않았습니다.")
        print("다시 입력해주세요")
        val1 = input_value1()

def input_value2():
    try:
        val2 = int(input("숫자2\n"))
        return val2
    except ValueError:
        print("숫자가 입력되지 않았습니다.")
        print("다시 입력해주세요")
        val2 = input_value2()

def cal(mode, val1, val2):
    if mode == "plus":
        result = val1 + val2
    elif mode == "minus":
        result = val1 - val2
    elif mode == "multiply":
        result = val1 * val2
    elif mode == "division":
        try:
            result = val1 / val2
        except ZeroDivisionError:
            print("0으로 나눗셈을 할 수 없습니다.")
            result = "NaN"
    else:
        print("알 수 없습니다.")
    return result
    
if __name__ == "__main__":
    while True:
        mode = mode_option()
        if mode == "quit":
            break
        val1 = input_value1()
        val2 = input_value2()
        result = cal(mode, val1, val2)
        print(result)
# 사용자로부터 점수 입력 받는다
# 사용자로부터 이름 입력 받는다
# 이 점수가 최고 점수면 하이 스코어를 기록한다.
# 1. high 라고 입력하면 현재까지의 하이 스코어와 그 사람이 누군지 출력한다
# 2. history 라고 입력하면 그 동안 입력한 모든 점수와 사람을 출력한다

def input_score():
    score = int(input("점수를 입력하세요\n"))
    name = input("이름을 입력하세요\n")
    return score, name

def store_result(score, name):
    game_score = (score, name)
    game_history.append(game_score)

def print_history():
    print(game_history)

def print_highscore():
    high = 0
    high_user = None
    for score, name in game_history:
        if score > high:
            high = score
            high_user = name
    print(high, high_user)

def mode_option():
    option = ["high", "history", "quit", "save"]
    selected_mode = input(f"모드를 입력하세요 {option}\n")
    return selected_mode

if __name__ == "__main__":
    game_history = []
    high_score = 0
    score, name = input_score()
    store_result(score, name)
    
    while True:
        mode = mode_option()
        if mode == "high":
            print_highscore()
        elif mode == "history":
            print_history()
        elif mode == "quit":
            break
        elif mode == "save":
            score, name = input_score()
            store_result(score, name)
            
# 3. 모듈화
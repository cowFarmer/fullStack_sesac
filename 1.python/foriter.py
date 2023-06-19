'''
사람 목록에서 사람 찾고
상점 목록에서 그 사람이 방문한 상점 찾고
그 안에 있는 물품 목록에서 주문한 물품 찾고
-> 너무 비효율적

효율성 매우 중요해짐 그래서 알고리즘으로 해결 하고자 함
-> 코딩 테스트 공부 하면서 찾아가기
시간복잡도 for문 2번 0(n^2), for문 3번은 0(n^3) -> 실무에서 사용 불가능
'''

def nested_loop():
    n = 10
    count = 0
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    count += 1
    print(count)                    
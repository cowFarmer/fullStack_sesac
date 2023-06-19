# word = '게맛살, 구멍, 글라이더, 기차, 대롱, 더치페이, 롱다리, 리본, 멍게, 박쥐, 본네트, 빨대, 살구, 양심, 이빨, 이자, 자율, 주기, 쥐구멍, 차박, 트라이앵글'
# print(word.replace(' ', '').split(','))
com_words = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', '멍게', \
                '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']

def word_chain(word):
    used_words = [word]
    status = 1
    com_word = word
    while True:
        # 컴퓨터 공격 시작
        if status == 1:
            print(f'<시작>끝말잇기 ㄱㄱ. {word}')
            com_words.remove(word)
            status = 2
            
        # 사용자 공격
        if status == 2:
            used_word = input('')
            # print(used_word)
            if com_word[-1] != used_word[0]:
                return '글자가 안 이어져. 내가 이겼다!<끝>'
            elif used_word in used_words:
                return '아까 했던 말이야. 내가 이겼어!<끝>'
            else:
                used_words.append(used_word)
                print(f'user = {used_word}')
                status = 3
                   
        # 컴퓨터 공격
        if status == 3:
            for com_word in com_words:
                if used_words[-1][-1] == com_word[0]:
                    print(f'computer = {com_word}')
                    com_words.remove(com_word)
                    used_words.append(com_word)
                    print(com_words)
                    print(used_words)
                    status = 2
            if status != 2:
                return '모르겠다. 내가 졌어.<끝>'

print(word_chain('기차'))
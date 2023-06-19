com_words = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', '멍게', \
                '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']

def word_chain(com_word):
    used_words = [com_word]
    print('<시작>끝말잇기 ㄱㄱ. 기차')
    com_words.remove(com_word)
    status = 1 # 1: user -> com, 2: com -> user
    
    while True:
        # 1 user -> com
        if status == 1:
            use_word = input('입력하세요 \n')
            if use_word == '':
                use_word = input('입력하세요 \n')
            print('-'*10)
            if use_word in used_words:
                return '아까 했던 말이야. 내가 이겼어!<끝>'
            elif use_word[0] != com_word[-1]:
                return '글자가 안 이어져. 내가 이겼다!<끝>'
            else:
                used_words.append(use_word)
            # 중복 제거 in com_words
            if use_word in com_words:
                com_words.remove(use_word)
                # print(com_words)
            print(f'user => {use_word}')
            status = 2
        
        # 2 com -> user
        if status == 2:
            for word in com_words:
                if use_word[-1] == word[0] and status != 1:
                    com_word = word
                    print(f'com => {com_word}')
                    used_words.append(com_word)
                    com_words.remove(com_word)
                    status = 1
            if status == 2:
                return '모르겠다. 내가 졌어.<끝>'
    
print(word_chain('기차'))
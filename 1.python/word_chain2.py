# 끝말잇기에 두음법칙 적용하기
rule_of_thumbs = '라락란랄람랍랑래랭냑략냥량녀려녁력년련녈렬념렴렵녕령녜례로록론롱뢰뇨료룡루뉴류뉵륙륜률륭륵름릉니리린림립'
trans_rule_of_thumbs = '나낙난날남납낭내냉약약양양여여역역연연열열염염엽영영예예노녹논농뇌요요용누유유육육윤율융늑늠능이이인임입'

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
            print('-'*10)
            if use_word in used_words:
                return '아까 했던 말이야. 내가 이겼어!<끝>'
            # 두음법칙 적용하고 넘어가려면 find 값이 같아야 함 -1이 됐든 숫자가 됐든
            elif use_word[0] != com_word[-1]:
                return '글자가 안 이어져. 내가 이겼다!<끝>'
            elif use_word[0] == com_word[-1] or rule_of_thumbs.find(com_word[-1]) == rule_of_thumbs.find(use_word[-1]):
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
                # 컴퓨터 두음법칙 적용
                if (use_word[-1] == word[0] or \
                    trans_rule_of_thumbs[rule_of_thumbs.find(use_word[-1])] == word[0]) and status != 1:
                    com_word = word
                    print(f'com => {com_word}')
                    used_words.append(com_word)
                    com_words.remove(com_word)
                    status = 1
            if status == 2:
                return '모르겠다. 내가 졌어.<끝>'
    
print(word_chain('기차'))
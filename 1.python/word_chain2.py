# 끝말잇기에 두음법칙 적용하기
rule_of_thumbs = '라락란랄람랍랑래랭냑략냥량녀려녁력년련녈렬념렴렵녕령녜례로록론롱뢰뇨료룡루뉴류뉵륙륜률륭륵름릉니리린림립'
trans_rule_of_thumbs = '나낙난날남납낭내냉약약양양여여역역연연열열염염엽영영예예노녹논농뇌요요용누유유육육윤율융늑늠능이이인임입'

com_words = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', '멍게', \
                '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']

def word_chain(word):
    user_words = []
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
            user_word = input('')
            print(user_word, com_word)
            if com_word[-1] != user_word[0]: # 두음법칙 적용하기
                return '글자가 안 이어져. 내가 이겼다!<끝>'
            elif user_word in user_words:
                return '아까 했던 말이야. 내가 이겼어!<끝>'
            else:
                user_words.append(user_word)
                print(f'user = {user_word}')
                status = 3
                   
        # 컴퓨터 공격
        if status == 3:
            for com_word in com_words:
                if user_words[-1][-1] == com_word[0]:
                    print(f'computer = {com_word}')
                    com_word = com_word
                    com_words.remove(com_word)
                    status = 2
                elif user_words[-1][-1] in rule_of_thumbs and trans_rule_of_thumbs[rule_of_thumbs.find(user_words[-1][-1])] == com_word[0]:
                    com_word = com_word
                    print(f'computer = {com_word}')
                    com_words.remove(com_word)
                    status = 2
            # for rule_word in rule_of_thumbs:
                # if user_words[-1][-1] in rule_word.keys():
                #     for com_word in com_words:
                #         if rule_word[user_words[-1][-1]] == com_word[0]:
                #             print(f'computer = {com_word}')
                #             com_words.remove(com_word)
                #             status = 2
            if status != 2:
                return '모르겠다. 내가 졌어.<끝>'

print(word_chain('기차'))
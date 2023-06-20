import datetime

# 각 모듈별 사용벙은 원작자들이 만든 메뉴얼 참조하기
# 개별 모듈이면 원작자 홈페이지, 패키지 다운로드 공식 사이트 참조
# NOT TO DO ->> 남의 글 참조하기 틀리거나 비효율적인 것들이 많음
# *** 원작자 원문 참조 ***
current_time = datetime.datetime.now()
                # 모듈명. 클래스명. 함수명

print("현재 시간", current_time)

specific_time = datetime.datetime(2023, 6, 20, 10, 30, 00)
print(f"내가 만든 날짜: {specific_time}")
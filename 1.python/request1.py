# 원하는 웹 페이지 가져오기
# 일반적으로 웹에 있는 컨텐츠를 가져오기 위해 GUI를 통해 사람이 반복 >> 불필요
# 코드를 통해 정보(contents) 가져와보자

import requests

response = requests.get('https://movie.daum.net/main')
# print(response.status_code)
# print(response.url)
# print(response.headers)
# print(response.text)

# 네이버 페이지 내에서 가져온 컨텐츠 중 <H2> 태그로 작성된 컨텐츠 출력하기
search_str = "h2"
contents = response.text

for line in contents.splitlines():
    # print(line)
    if search_str in line:
        print(line.strip())
import os
import sys
import urllib.request
import json


client_id = "HEr1BPvvAN_IR37i7Ak7"
client_secret = open("secret.txt", "r").read()

encText = urllib.parse.quote("sqlalchemy")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    
    data = json.loads(response_body)
    print(data)
else:
    print("Error Code:" + rescode)
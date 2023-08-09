import urllib.request
import json

client_id = "HEr1BPvvAN_IR37i7Ak7"
client_secret = open("secret.txt", "r").read()

def translation_ko_to_en(sentence):
    data = "source=ko&target=en&text=" + sentence
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        data = json.loads(response_body)
        result = data['message']['result']['translatedText']
    else:
        result = sentence
    
    return result
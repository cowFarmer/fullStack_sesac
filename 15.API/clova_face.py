import os
import sys
import requests
import cv2
import numpy as np
import json


def clova_face(filename):
    client_id = "HEr1BPvvAN_IR37i7Ak7"
    client_secret = open("secret.txt", "r").read()

    url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    # url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

    
    files = {'image': open(filename, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        # print(response.text)
        data = json.loads(response.text)
        face_info = []
        for i in range(len(data['faces'])):
            face_info.append(data['faces'][i])
        return face_info
    else:
        print("Error Code:" + rescode)
        
def my_opencv(filename):
    face_info = clova_face(filename)
    image = cv2.imread(filename)
    
    # cv2.rectangle(image, )
    for i in range(len(face_info)):
        x, y, w, h = face_info[i]['roi']['x'], face_info[i]['roi']['y'], face_info[i]['roi']['width'], face_info[i]['roi']['height']
        cv2.rectangle(image, (x, y), (x+w, y+h), (244, 133, 66), 3)
        
        # gender, 나이, 감정 
        gender = face_info[i]['gender']['value']
        cv2.putText(image, gender, (x, y+h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (67, 53, 234), 1)
        age = face_info[i]['age']['value']
        cv2.putText(image, age, (x, y+h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (67, 53, 234), 1)
        emotion = face_info[i]['emotion']['value']
        cv2.putText(image, emotion, (x, y+h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (67, 53, 234), 1)
        print(gender, age, emotion)
        
    cv2.imshow('kim', image)
    cv2.waitKey(0)
        
if __name__ == "__main__":
    filename = f"images/김병만.jpg"
    
    # clova_face(filename)
    my_opencv(filename)
import os

data = "hello world \n"
filepath = "./data/"
filename = "myfile.txt"


try:
    with open(filepath+filename, "a") as file:
        file.write(data)
        print("파일쓰기완료")
        
except:
    print("file not found")
    os.mkdir(filepath)
    
    
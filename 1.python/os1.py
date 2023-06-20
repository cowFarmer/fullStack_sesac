import os

current_dir = os.getcwd() # -> CWD > current working directory
# print(f"현재 디렉토리: {current_dir}")

# for i in range(0, 10):
    # 폴더 만들기
    # os.mkdir(f"sesac{i}")
    # 폴더 삭제
    # os.rmdir(f"sesac{i}")
    
# 환경 변수 출력
python_path = os.getenv("PATH")
# print(python_path)

# 터미널 명령어 실행
os.system("ls")
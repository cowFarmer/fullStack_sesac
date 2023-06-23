import random
from manager.read_file import ReadFile

class GenerateName:
    def __init__(self):
        self.last_names = []
        self.first_names = []
        
        # 참조하는 txt 파일 읽기
        self.last_names = ReadFile("last_names.txt", self.last_names).read()
        self.first_names = ReadFile("first_names.txt", self.first_names).read()
    
    def get_name(self):
        return random.choice(self.last_names)+random.choice(self.first_names)
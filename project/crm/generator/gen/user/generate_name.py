import random
from manager.read_file import ReadFile

class GenerateName:
    _instance = None
    
    def __init__(self):
        if GenerateName._instance is None:
            GenerateName._instance = GenerateName()
            self.last_names = ReadFile("last_names.csv", self.last_names).read()
            self.first_names = ReadFile("first_names.csv", self.first_names).read()
    
    def get_name(self):
        return random.choice(self.last_names)+random.choice(self.first_names)
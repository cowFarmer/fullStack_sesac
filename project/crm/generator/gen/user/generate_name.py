import random
from manager.read_file import ReadFile

class GenerateName:
    _instance = None
    last_names = None
    first_names = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.last_names = ReadFile("last_names.csv").read()
            cls.first_names = ReadFile("first_names.csv").read()
        return cls._instance
    
    def get_name(self):
        return random.choice(self.last_names) + random.choice(self.first_names)
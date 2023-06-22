import random

class GenerateStoreName:
    def __init__(self, store):
        self.store = store
    
    def get_type(self):
        return f"{self.store} {random.randint(1,15)}호점"
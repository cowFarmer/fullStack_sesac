import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('movie.sqlite', check_same_thread=False)
        self.cursor = self.db.cursor()
        
    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        
    def execute_fetch(self, query, args={}):
        self.cursor.execute(query, args)
        result = self.cursor.fetchall()
        return result
        
    def commit(self):
        self.db.commit()
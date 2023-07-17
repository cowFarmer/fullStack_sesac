import sqlite3


class DatabaseController:
    def __init__(self):
        self.db_location = "model/database/crm.db"
        self.conn = None
        self.c = None
    
    def connect(self):
        self.conn = sqlite3.connect(self.db_location)
        self.c = self.conn.cursor()
        
    def connect_row(self):
        self.conn = sqlite3.connect(self.db_location)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
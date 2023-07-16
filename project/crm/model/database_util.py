import sqlite3


class ConnectDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("model/database/crm.db")
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
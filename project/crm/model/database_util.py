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
    
    def get_header_from_table(self, table=None):
        if table == None:
            raise ValueError
        self.connect()
        query = f"SELECT * FROM {table}"
        self.c.execute(query)
        header = [row[0] for row in self.c.description]
        return header
    
    def get_data_from_query(self, query=None):
        '''
        return list[dict] form
        '''
        
        self.connect_row()
        if query == None:
            raise ValueError
        self.c.execute(query)
        data = self.c.fetchall()
        result = [dict(d) for d in data]
        return result
import uuid
import datetime

from model.database_util import DatabaseController


# arg로 받아온 user_id가 None이면 uuid 생성
non_member_uuid = uuid.uuid4()

class OrderedAppend(DatabaseController):
    def __init__(self):
        self.ordered_id = str(uuid.uuid4())
        
        self.tmp_user_id = str(uuid.uuid4())
        self.date_time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def kiosk_data(self, **kwargs):
        if kwargs["user_id"] == None:
            self.user_id = self.tmp_user_id
        else:
            self.user_id = kwargs["user_id"]
        self.store_id = kwargs["store_id"]
        self.update_db()
        pass
    
    def update_db(self):
        table_name = "ordered"
        id = self.ordered_id
        order_at = self.date_time_now
        store_id = self.store_id
        user_id = self.user_id
        
        self.connect()
        # sql_query = f'''
        # UPDATE {table_name}
        # '''
        self.commit()
        self.close()
        pass

class OrderitemAppend(DatabaseController):
    def __init__(self):
        self.orderitem_id = str(uuid.uuid4())
        
    def kiosk_data(self, **kwargs):
        
        self.update_db()
        pass
    
    def update_db(self, item_id, ordered_id):
        table_name = "orderitem"
        id = self.orderitem_id
        order_id = ordered_id
        item_id = item_id
        
        self.connect()
        # sql_query = f'''
        # UPDATE {table_name}
        # c.execute('''INSERT INTO users2(username, password) VALUES(?, ?)''', (u[0], hash_password(u[1])))
        # '''
        self.commit()
        self.close()
        pass
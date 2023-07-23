import uuid
import datetime

from model.database_util import DatabaseController


# arg로 받아온 user_id가 None이면 uuid 생성
non_member_uuid = uuid.uuid4()

class OrderedAppend(DatabaseController):
    def __init__(self):
        super().__init__()
        
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
    
    def update_db(self):
        table_name = "ordered"
        id = self.ordered_id
        order_at = self.date_time_now
        store_id = self.store_id
        user_id = self.user_id
        
        self.connect()
        sql_query = f'''
        INSERT INTO {table_name} (Id, OrderAt, StoreId, UserId) VALUES(?, ?, ?, ?)
        '''
        self.c.execute(sql_query, (id, order_at, store_id, user_id))
        self.commit()
        self.close()
        
    def get_ordered_id(self):
        return self.ordered_id

class OrderitemAppend(DatabaseController):
    def __init__(self):
        super().__init__()
        
        self.orderitem_id = str(uuid.uuid4())
        
    def kiosk_data(self, **kwargs):
        order_id = kwargs["order_id"]
        item_id = kwargs["item_id"]
        self.update_db(order_id, item_id)
    
    def update_db(self, order_id, item_id):
        table_name = "orderitem"
        id = self.orderitem_id
        order_id = order_id
        item_id = item_id
        
        self.connect()
        sql_query = f'''
        INSERT INTO {table_name} (Id, OrderId, ItemId) VALUES(?, ?, ?)
        '''
        self.c.execute(sql_query, (id, order_id, item_id))
        self.commit()
        self.close()
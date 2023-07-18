from model.query_util import QueryUtil


class UserDetail(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
        
    def user_info(self, **kwargs):
        data = self.dict_filter(kwargs)
        user_id = data["id"]
        
        self.query = f'''
        SELECT *
        FROM user
        WHERE user.id LIKE '{user_id}';
        '''
        
        result = self.get_data_from_query(self.query)
        return result
        
    def user_transaction_history(self, **kwargs):
        data = self.dict_filter(kwargs)
        user_id = data["id"]
        
        self.query = f'''
        SELECT ordered.Id, ordered.OrderAt, ordered.StoreId
        FROM user
        JOIN ordered ON user.id = ordered.UserId
        WHERE ordered.UserId LIKE '{user_id}'
        ORDER BY ordered.OrderAt DESC;
        '''
        
        result = self.get_data_from_query(self.query)
        return result
    
    def user_item_count_order(self, **kwargs):
        data = self.dict_filter(kwargs)
        user_id = data["id"]
        
        self.query = f'''
        SELECT item.name, COUNT(*) AS "total_count"
        FROM user
        JOIN ordered ON user.Id = ordered.UserId
        JOIN store ON ordered.StoreId = store.Id
        JOIN orderitem ON ordered.Id = orderitem.OrderId
        JOIN item ON orderitem.ItemId = item.Id
        WHERE user.id = "{user_id}"
        GROUP BY item.id
        ORDER BY "total_count" DESC
        LIMIT 5;
        '''
        header = self.get_header_from_query(self.query)
        result = self.get_data_from_query(self.query)
        return header, result
    
    def user_store_count_order(self, **kwargs):
        data = self.dict_filter(kwargs)
        user_id = data["id"]
        
        self.query = f'''
        SELECT store.name, COUNT(*) AS "total_count"
        FROM user
        JOIN ordered ON user.Id = ordered.UserId
        JOIN store ON ordered.StoreId = store.Id
        JOIN orderitem ON ordered.Id = orderitem.OrderId
        JOIN item ON orderitem.ItemId = item.Id
        WHERE user.id = "{user_id}"
        GROUP BY store.id
        ORDER BY "total_count" DESC
        LIMIT 5;
        '''
        header = self.get_header_from_query(self.query)
        result = self.get_data_from_query(self.query)
        return header, result
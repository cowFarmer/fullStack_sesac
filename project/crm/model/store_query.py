from model.query_util import QueryUtil

class StoreSearch(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
        
    def search_store(self, **kwargs):
        data = self.dict_filter(kwargs)
        
        search_page = data["search_page"]
        self.per_page = data["per_page"]
        
        offset_num = (search_page - 1) * self.per_page
        offset = f"OFFSET {offset_num}"
        limit = f"LIMIT {self.per_page}"
        
        self.query += '''
        SELECT *
        FROM store
        '''
        
        count = self.search_count_from_query(self.query)
        
        self.query += self.query_limit_offset(limit, offset)
        self.query += self.query_end()
        
        store_item = self.get_data_from_query(self.query)
        
        return store_item, count
        

class StoreDetail(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
        
    def store_info(self, **kwargs):
        data = self.dict_filter(kwargs)
        store_id = data["id"]
        
        self.query = f'''
        SELECT store.name, store.type, store.address
        FROM store
        WHERE store.id LIKE '{store_id}';
        '''
        
        store_header = self.get_header_from_query(self.query)
        store_data = self.get_data_from_query(self.query)
        
        return store_header, store_data
    
    def store_transaction_history_per_month(self, **kwargs):
        data = self.dict_filter(kwargs)
        store_id = data["id"]
        
        # store의 월간 매출액
        self.query = f'''
        SELECT strftime("%Y-%m", ordered.OrderAt) AS "month", SUM(item.UnitPrice) AS "total revenue", COUNT(orderitem.ItemId) AS "total count"
        FROM store
        JOIN ordered ON store.Id = ordered.StoreId
        JOIN orderitem ON ordered.Id = orderitem.OrderId
        JOIN item ON orderitem.ItemId = item.Id
        WHERE store.id LIKE "{store_id}"
        GROUP BY "month"
        '''
        
        result_header = self.get_header_from_query(self.query)
        result_data = self.get_data_from_query(self.query)
        
        return result_header, result_data
    
    def store_transaction_history_regular_customer(self, **kwargs):
        data = self.dict_filter(kwargs)
        store_id = data["id"]
        
        # store의 단골 고객
        # 나중에 date 범위 넣어서 부분만 보여줄 수 있을듯
        # WHERE ordered.OrderAt BETWEEN strftime("%Y-%m-%d", ordered.OrderAt) AND strftime("%Y-%m-%d", ordered.OrderAt)
        # WHERE ordered.OrderAt BETWEEN strftime("{start_date}", ordered.OrderAt) AND strftime("{end_date}", ordered.OrderAt)
        self.query = f'''
        SELECT user.Id, user.Name, SUM(item.UnitPrice) AS "total revenue", COUNT(orderitem.ItemId) AS "frequency"
        FROM store
        JOIN ordered ON store.Id = ordered.StoreId
        JOIN orderitem ON ordered.Id = orderitem.OrderId
        JOIN user ON ordered.UserId = user.Id
        JOIN item ON orderitem.ItemId = item.Id
        WHERE store.id LIKE "{store_id}"
        GROUP BY user.Id
        ORDER BY "frequency" DESC;
        '''
        
        result_header = self.get_header_from_query(self.query)
        result_data = self.get_data_from_query(self.query)
        
        return result_header, result_data
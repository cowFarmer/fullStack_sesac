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
    
    def store_transaction_history(self, **kwargs):
        data = self.dict_filter(kwargs)
        item_id = data["id"]
        
        self.query = f'''
        
        '''
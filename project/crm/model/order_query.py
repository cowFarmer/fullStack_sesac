from model.query_util import QueryUtil

class OrderSearch(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
        
    def search_order(self, **kwargs):
        data = self.dict_filter(kwargs)
        
        search_page = data["search_page"]
        self.per_page = data["per_page"]
        
        offset_num = (search_page - 1) * self.per_page
        offset = f"OFFSET {offset_num}"
        limit = f"LIMIT {self.per_page}"
        
        self.query += '''
        SELECT *
        FROM ordered
        '''
        
        count = self.search_count_from_query(self.query)
        
        self.query += self.query_limit_offset(limit, offset)
        self.query += self.query_end()
        
        order_item = self.get_data_from_query(self.query)
        
        return order_item, count
        
class OrderItemSearch(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
        
    def search_order_item(self, **kwargs):
        data = self.dict_filter(kwargs)
        
        search_page = data["search_page"]
        self.per_page = data["per_page"]
        
        offset_num = (search_page - 1) * self.per_page
        offset = f"OFFSET {offset_num}"
        limit = f"LIMIT {self.per_page}"
        
        self.query += '''
        SELECT *
        FROM orderitem
        '''
        
        count = self.search_count_from_query(self.query)
        
        self.query += self.query_limit_offset(limit, offset)
        self.query += self.query_end()
        
        order_item = self.get_data_from_query(self.query)
        
        return order_item, count

class OrderDetailSearch(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
    
    def search_order_id(self, **kwargs):
        data = self.dict_filter(kwargs)
        order_id = data["id"]
        
        self.query += f'''
        SELECT orderitem.Id, orderitem.OrderId, ordered.OrderAt, orderitem.ItemId, item.Name
        FROM ordered
        JOIN orderitem ON ordered.Id = orderitem.OrderId
        JOIN item ON orderitem.ItemId = item.Id
        WHERE ordered.Id LIKE '{order_id}';
        '''
        header = self.get_header_from_query(self.query)
        result = self.get_data_from_query(self.query)
        return header, result
        
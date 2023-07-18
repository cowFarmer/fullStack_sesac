from model.query_util import QueryUtil


class ItemSearch(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
        
    def search_item(self, **kwargs):
        data = self.dict_filter(kwargs)
        
        self.query += '''
        SELECT *
        FROM item;
        '''
        
        item_header = self.get_header_from_table("item")
        item_data = self.get_data_from_query(self.query)
        
        return item_header, item_data
    
class ItemDetail(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
    
    def item_info(self, **kwargs):
        data = self.dict_filter(kwargs)
        item_id = data["id"]
        
        self.query = f'''
        SELECT item.Name, item.UnitPrice
        FROM item
        WHERE item.id LIKE '{item_id}';
        '''
        
        item_header = self.get_header_from_query(self.query)
        item_data = self.get_data_from_query(self.query)
        
        return item_header, item_data
    
    def item_transaction_history(self, **kwargs):
        data = self.dict_filter(kwargs)
        item_id = data["id"]
        
        self.query = f'''
        SELECT strftime("%Y-%m", ordered.OrderAt) AS "month", SUM(item.UnitPrice) AS "total revenue", COUNT(orderitem.ItemId) AS "total count"
        FROM Item
        JOIN orderitem ON item.Id = orderitem.ItemId
        JOIN ordered ON orderitem.OrderId = ordered.Id
        WHERE item.id LIKE '{item_id}'
        GROUP BY item.Id, strftime("%Y-%m", ordered.OrderAt)
        ORDER BY ordered.OrderAt ASC;
        '''
        
        item_header = self.get_header_from_query(self.query)
        item_data = self.get_data_from_query(self.query)
        
        return item_header, item_data
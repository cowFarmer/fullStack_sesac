import math

from utils.database_util import ConnectDatabase
from utils.page.pagelist import pageList


class QueryManager(ConnectDatabase):
    def __init__(self):
        super().__init__()
    
    def get_db_from_query(self, query=None):
        '''
        return list[dict] form
        '''
        if query == None:
            raise ValueError
        self.c.execute(query)
        data = self.c.fetchall()
        
        result = [dict(d) for d in data]
        header = result[0].keys()
        return header, result
    
    # user용 filter 추가 하지만 좋지 않아 보임
    def dict_filter(_, data: dict):
        result = {}
        for key in data:
            if data[key] != "":
                # user 전용 search_age_group
                if key == "search_age_group" and data[key] == 0:
                    continue
                result[key] = data[key]
        return result
    
    # USER QUERY
    def search_user(self, **kwargs):
        data = self.dict_filter(kwargs)
        
        search_page = data["search_page"]
        per_page = data["per_page"]
        
        offset_num = (search_page - 1) * per_page
        offset = f"OFFSET {offset_num}"
        limit = f"LIMIT {per_page}"
        
        query = f'''
        SELECT *
        FROM USER
        '''
        
        try:
            search_name = data["search_name"]
            query += f"WHERE user.name LIKE '%{search_name}%'"
        except:
            pass
        
        query += f'''
        {limit}
        {offset};
        '''
        return query
    
    # TODO count_total을 search_user에 넣어야 한다
    def count_total(cls, table, per_page):
        query = f'''
        SELECT COUNT(*) AS total
        FROM {table};
        '''
        _, total_data = cls.get_db_from_query(query)
        total_page = math.ceil(total_data[0]["total"] / per_page)
        return total_page
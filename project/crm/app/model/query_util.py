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
    
    # TEST 디버깅용
    def get_count_from_query(self, query=None):
        if query == None:
            raise ValueError
        self.c.execute(query)
        data = self.c.fetchall()
        result = [dict(d) for d in data]
        return result        
    
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
        
        try:
            if "WHERE" in query:
                search_gender = data["search_gender"]
                query += f"AND user.gender LIKE '{search_gender}'"
            else:
                search_gender = data["search_gender"]
                query += f"WHERE user.gender LIKE '{search_gender}'"
        except:
            pass
        
        try:
            if "WHERE" in query:
                search_age_group = data["search_age_group"]
                query += f"AND user.age BETWEEN '{search_age_group}' AND '{search_age_group + 9}'"
            else:
                search_age_group = data["search_age_group"]
                query += f"WHERE user.age BETWEEN '{search_age_group}' AND '{search_age_group + 9}'"
        except:
            pass
        
        query += f'''
        {limit}
        {offset};
        '''
        return query
    
    def search_user_count(self, **kwargs):
        data = self.dict_filter(kwargs)
        
        per_page = data["per_page"]
        
        query = f'''
        SELECT COUNT(*) AS "total_count"
        FROM USER
        '''
        
        try:
            search_name = data["search_name"]
            query += f"WHERE user.name LIKE '%{search_name}%'"
        except:
            pass
        
        try:
            if "WHERE" in query:
                search_gender = data["search_gender"]
                query += f"AND user.gender LIKE '{search_gender}'"
            else:
                search_gender = data["search_gender"]
                query += f"WHERE user.gender LIKE '{search_gender}'"
        except:
            pass
        
        try:
            if "WHERE" in query:
                search_age_group = data["search_age_group"]
                query += f"AND user.age BETWEEN '{search_age_group}' AND '{search_age_group + 9}'"
            else:
                search_age_group = data["search_age_group"]
                query += f"WHERE user.age BETWEEN '{search_age_group}' AND '{search_age_group + 9}'"
        except:
            pass
        
        query += f'''
        ;
        '''
        
        _, total_data = self.get_db_from_query(query)
        
        for d in total_data:
            total_count = d.get("total_count")
            
        total_page = math.ceil(total_count / per_page)
        return total_page
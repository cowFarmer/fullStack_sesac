import math

from model.query_util import QueryUtil


class UserSearch(QueryUtil):
    def __init__(self):
        super().__init__()
        self.query = ""
        
    
    def search_user(self, **kwargs):
        # args 필터링
        data = self.dict_filter(kwargs)
        
        search_page = data["search_page"]
        self.per_page = data["per_page"]
    
        offset_num = (search_page - 1) * self.per_page
        offset = f"OFFSET {offset_num}"
        limit = f"LIMIT {self.per_page}"
        
        self.query += f"{self.query_select()}"
        self.query += f"{self.query_from('user')}"
        
        if "search_name" in data:
            # WHERE user.name LIKE '%search_name%'
            self.query += self.query_where_like_include("user", "name", data["search_name"], self.query)
            
        if "search_gender" in data:
            # WHERE user.gender like 'search_gender'
            self.query += self.query_where_like("user", "gender", data["search_gender"], self.query)
            
        if "search_age_group" in data:
            self.query += self.query_where_between(self.query, "user", "age", data["search_age_group"], mode="search_age_group")
        
        count = self.search_count_from_query(self.query)
        
        self.query += self.query_limit_offset(limit, offset)
        self.query += self.query_end()
        
        result = self.get_data_from_query(self.query)
        return result, count
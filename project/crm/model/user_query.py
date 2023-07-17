import math

from model.query_util import QueryManager


class UserSearch(QueryManager):
    def __init__(self):
        super().__init__()
        self.query = f'''
        SELECT *
        FROM USER
        '''
    
    def search_user(self, **kwargs):
        # args 필터링
        data = self.dict_filter(kwargs)
        
        search_page = data["search_page"]
        self.per_page = data["per_page"]
    
        offset_num = (search_page - 1) * self.per_page
        offset = f"OFFSET {offset_num}"
        limit = f"LIMIT {self.per_page}"
        
        # TODO: 정리하기
        # 방법 1. 각 쿼리문 조회를 함수로 빼기
        # 방법 2. list에 append하고 마지막에 for문 돌면서 추가하기
        try:
            search_name = data["search_name"]
            self.query += f"WHERE user.name LIKE '%{search_name}%'"
        except:
            pass
        
        try:
            if "WHERE" in self.query:
                search_gender = data["search_gender"]
                self.query += f"AND user.gender LIKE '{search_gender}'"
            else:
                search_gender = data["search_gender"]
                self.query += f"WHERE user.gender LIKE '{search_gender}'"
        except:
            pass
        
        try:
            if "WHERE" in self.query:
                search_age_group = data["search_age_group"]
                self.query += f"AND user.age BETWEEN '{search_age_group}' AND '{search_age_group + 9}'"
            else:
                search_age_group = data["search_age_group"]
                self.query += f"WHERE user.age BETWEEN '{search_age_group}' AND '{search_age_group + 9}'"
        except:
            pass
        
        count = self.search_user_count(self.query)
        
        self.query += f'''
        {limit}
        {offset}
        ;
        '''
        
        result = self.get_data_from_query(self.query)
        return result, count

    def search_user_count(self, query):
        query = query.replace("SELECT *", "SELECT COUNT(*) AS 'total_count'")
        
        data = self.get_data_from_query(query)
        
        for d in data:
            total_count = d.get("total_count")
        
        total_count = math.ceil(total_count / self.per_page)
        
        return total_count
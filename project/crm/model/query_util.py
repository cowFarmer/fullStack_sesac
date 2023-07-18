import math

from model.database_util import DatabaseController


class QueryUtil(DatabaseController):
    def __init__(self):
        super().__init__()
    
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
    
    def get_header_from_table(self, table=None):
        '''
        return [str]
        '''
        if table == None:
            raise ValueError
        self.connect()
        query = f"SELECT * FROM {table} "
        self.c.execute(query)
        header = [row[0].lower() for row in self.c.description]
        return header
    
    def get_header_from_query(self, query=None):
        if query == None:
            raise ValueError
        self.connect()
        self.c.execute(query)
        header = [row[0].lower() for row in self.c.description]
        return header
    
    def get_data_from_query(self, query=None):
        '''
        return [{}]
        '''
        if query == None:
            raise ValueError
        self.connect_row()
        self.c.execute(query)
        data = self.c.fetchall()
        result = [dict(d) for d in data]
        result = [{k.lower(): v for k, v in row.items()} for row in result]
        return result
    
    def get_one_data_from_query(self, query=None):
        '''
        return [{}]
        '''
        if query == None:
            raise ValueError
        self.connect_row()
        self.c.execute(query)
        data = self.c.fetchone()
        result = [dict(d) for d in data]
        result = [{k.lower(): v for k, v in row.items()} for row in result]
        return result
    
    def query_select(self, param=None):
        if param == None:
            return "SELECT * "
        return f"SELECT {param}"
        
    def query_select_count(self, param=None):
        if param == None:
            return "SELECT COUNT(*) "
        return f"SELECT COUNT({param})"
    
    def query_from(self, table):
        return f"FROM {table} "
    
    def query_join(self, base, base_feature, target, target_feature):
        return f"JOIN {target} ON {base}.{base_feature} = {target}.{target_feature} "
    
    def query_offset(self, offset_num=int):
        return f"OFFSET {offset_num} "
    
    def query_limit(self, limit_num=int):
        return f"LIMIT {limit_num} "
    
    def query_where_like(self, table, feature, search, query=None):
        if "WHERE" in query:
            return f"AND {table}.{feature} LIKE '{search}' "
        else:
            return f"WHERE {table}.{feature} LIKE '{search}' "
    
    def query_where_like_include(self, table, feature, search, query=None):
        if "WHERE" in query:
            return f"AND {table}.{feature} LIKE '%{search}%' "
        else:
            return f"WHERE {table}.{feature} LIKE '%{search}%' "
    
    def query_where_between(self, query, table, feature, search, mode=None):
        if mode == "search_age_group":
            if "WHERE" in query:
                return f"AND {table}.{feature} BETWEEN {search} AND {search + 9} "
            else:
                return f"WHERE {table}.{feature} BETWEEN {search} AND {search + 9} "
        else:
            print("QueryUtil.query_where_between 확인하세요")
            
    def query_limit_offset(self, limit, offset):
        return f"{limit} {offset}"
    
    def query_end(self):
        return ";"
    
    def search_count_from_query(self, query):
        query = query.replace("SELECT *", "SELECT COUNT(*) AS 'total_count'")
        data = self.get_data_from_query(query)
        for d in data:
            total_count = d.get("total_count")
        
        total_count = math.ceil(total_count / self.per_page)
        
        return total_count
from model.database_util import ConnectDatabase


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
        header = [d.lower() for d in header]
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
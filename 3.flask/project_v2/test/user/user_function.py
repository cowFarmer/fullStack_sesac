from functions.controller import ReadCsvDict
from functions.page.page_function import pageList
import math

def filter_user_file(filename=None, search_info=None, per_page=100, current_page=None):
    data = []
    search_info_filter = {}
    headers, lines = ReadCsvDict.file_name(filename=filename)
        
    # search_info filtering
    if search_info != None:
        for key, value in search_info.items():
            if value != "":
                search_info_filter[key] = value
        if search_info["age_group"] == 0:
            search_info_filter.pop("age_group")
    
    if len(search_info_filter) == 0 or search_info == None:
        for line in lines:
            data.append(line)
    else:
        # name 먼저 필터링
        if "name" in search_info_filter.keys():
            data = []
            for line in lines:
                if search_info_filter["name"] in line["name"]:
                    data.append(line)
            search_info_filter.pop("name")
            lines = data
        
        # group_age 필터링
        if "age_group" in search_info_filter.keys():
            data = []
            age_group_value = search_info_filter.get("age_group")
            age_filter = {"age_group": [str(_) for _ in range(age_group_value, age_group_value+10)]}
            for line in lines:
                if line["age"] in age_filter["age_group"]:
                    data.append(line)
            search_info_filter.pop("age_group")
            lines = data
        
        # value가 같은 경우 모두 비교
        if len(search_info_filter) > 0:
            data = []
            for line in lines:
                if all(line.get(key) == value for key, value in search_info_filter.items()):
                    data.append(line)
    
    total_page = math.ceil((len(data) / per_page))
    data_start_index = per_page * (current_page - 1)
    data_end_index = data_start_index + per_page
    slice_page_data = data[data_start_index:data_end_index]
    page_list = pageList(total_page, current_page)
        
    return headers, total_page, slice_page_data, page_list
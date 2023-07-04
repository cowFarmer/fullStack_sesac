def check_data_same_feather(datas, data_feather, check_datas, check_data_feather):
    tmp = []
    for check_data in check_datas:
        for data in datas:
            if data[data_feather] == check_data[check_data_feather]:
                tmp.append(check_data)
    return tmp

check_data_same_feather()
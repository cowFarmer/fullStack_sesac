import csv


class DictLower:
    def key_lower(lines):
        data = []
        for line in lines:
            tmp = {key.lower(): value.lower() for key, value in line.items()}
            data.append(tmp)
        return data
    
class ReadCsvDict:
    def file_name(filename=None):
        if filename == None:
            return print("읽을 파일 이름을 넣어주세요")
        with open(filename, "r") as file:
            lines = csv.DictReader(file, skipinitialspace=True)
            lines = DictLower.key_lower(lines)
            headers = lines[0].keys()
        return headers, lines
    
class CheckData:
#  말 그대로 data check해서 조건에 맞으면 list(dict) return
    def __init__(self):
        self.processed_data = []
    
    def check(self, datas):
        for data in datas:
            self.processed_data.append(data)
        return self.processed_data
    
    def check_id(self, id, new_datas, new_feature):
        for check_data in new_datas:
            if id == check_data[new_feature]:
                self.processed_data.append(check_data)
                continue
        return self.processed_data
    
    def check_same_feature(self, org_datas, org_feature, new_datas, new_feature):
        # org_datas, new_datas를 list(dict) 형태로 받아야 함
        for new_data in new_datas:
            for org_data in org_datas:
                if new_data[new_feature] == org_data[org_feature]:
                    self.processed_data.append(new_data)
        return self.processed_data
    
    def check_total_price(self, org_datas, new_datas):
        total_price = 0
        for new_data in new_datas:
            for org_data in org_datas:
                if org_data["id"] == new_data["itemid"]:
                    total_price += int(org_data["unitprice"])
                    self.processed_data.append(new_data)
        return total_price, self.processed_data
    
    def total_price(self, items):
        total_price = 0
        for item in items:
            total_price += int(item["unitprice"])
        return total_price
    
    def check_date(self, datas, start_date, end_date):
        success_flag = True
        if start_date == "":
            start_date = "0000-00-00"
        if end_date == "":
            end_date = "9999-99-99"
        if start_date > end_date:
            success_flag = False
        else:
            for data in datas:
                data_date = data["orderat"].split(" ")[0]
                if start_date <= data_date <= end_date:
                    self.processed_data.append(data)
                    
        return self.processed_data, success_flag
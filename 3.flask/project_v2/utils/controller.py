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
    
#  말 그대로 data check해서 조건에 맞으면 list(dict) return
class CheckData:
    def __init__(self):
        self.tmp = []
    
    def check(self, datas):
        for data in datas:
            self.tmp.append(data)
        return self.tmp
    
    def check_id(self, id, new_datas, new_feature):
        for check_data in new_datas:
            if id == check_data[new_feature]:
                self.tmp.append(check_data)
                continue
        return self.tmp
    
    def check_same_feature(self, og_datas, og_feature, new_datas, new_feature):
        # og_datas, new_datas를 list(dict) 형태로 받아야 함
        for new_data in new_datas:
            for og_data in og_datas:
                if new_data[new_feature] == og_data[og_feature]:
                    self.tmp.append(new_data)
        return self.tmp
    
    def check_total_price(self, og_datas, new_datas):
        total_price = 0
        for new_data in new_datas:
            for og_data in og_datas:
                if og_data["id"] == new_data["itemid"]:
                    total_price += int(og_data["unitprice"])
                    self.tmp.append(new_data)
        return total_price, self.tmp
    
    def total_price(self, items):
        total_price = 0
        for item in items:
            total_price += int(item["unitprice"])
        return total_price
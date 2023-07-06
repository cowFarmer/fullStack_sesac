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
        # TODO tmp 수정
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
    
    def check_date(self, datas, start_date, end_date):
        result_flag = True
        # TODO 코드 간소화 필요
        # 1. 둘다 비어 있는 경우 다 출력
        if start_date == "" and end_date == "":
            for data in datas:
                self.tmp.append(data)
        
        # 3. start_date가 비어 있는 경우
        if start_date == "":
            for data in datas:
                data_date = data["orderat"].split(" ")[0]
                if data_date <= end_date:
                    self.tmp.append(data)
        
        # 4. end_date가 비어 있는 경우
        if end_date == "":
            for data in datas:
                data_date = data["orderat"].split(" ")[0]
                if data_date >= start_date:
                    self.tmp.append(data)
        
        # 2. 일반적인 상황과 동일
        if start_date <= end_date:
            for data in datas:
                data_date = data["orderat"].split(" ")[0]
                if start_date <= data_date <= end_date:
                    self.tmp.append(data)
        
        # 5. 에러로 잘못 넘겨준 경우 -> start_date > end_date
        if start_date > end_date:
            result_flag = False

        return self.tmp, result_flag
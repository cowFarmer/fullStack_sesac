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
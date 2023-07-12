import csv


class ReadFile:
    def __init__(self, filename, target_feature=None):
        self.filename = filename
        self.append_list = []
        self.target_feature = target_feature
    
    def read(self):
        with open("./src/" + self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                self.append_list.append(line.strip())
        file.close()
        return list(set(self.append_list))

    def read_feature(self):
        data = []
        
        if self.target_feature == None:
            raise ValueError("read_feature 함수의 target_feature를 확인해주세요")
        else:
            with open("./save/" + self.filename + ".csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row[self.target_feature])
            return data
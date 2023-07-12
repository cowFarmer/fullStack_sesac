import csv

filename = "user"
target_feature = "Id"

data = []

def read_feature(filename, target_feature):
        with open("./save/" + filename + ".csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row[target_feature])
        return data

print(read_feature(filename, target_feature))
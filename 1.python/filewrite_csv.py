# csv -> comma seperated value
import csv

data = [
    ("name", "age", "city"),
    ("join", 25, "seoul"),
    ("bill", 20, "busan"),
    ("kim", 22, "seoul"),
]

filepath = "./data/"
filename = "user.csv"

with open(filepath+filename, "w", newline="\n") as file:
    csv_file = csv.writer(file)
    csv_file.writerows(data)

print("csv file written")
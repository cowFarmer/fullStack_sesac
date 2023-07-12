import csv

class WriterData:
    def write_data(self, data, category):
        with open("./save/" + category + ".csv", "w", newline="\n") as file:
            # TODO: category에 따른 header 추가하기
            csv_file = csv.writer(file)
            # csv_file.writerow(header)
            for d in data:
                csv_file.writerow(d)
            file.close()
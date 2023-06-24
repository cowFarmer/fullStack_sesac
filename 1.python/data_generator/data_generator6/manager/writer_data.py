import csv

class WriterData:
    def write_data(self, datas, save_file_name, category):
        with open("./save/" + save_file_name, "w", newline="\n") as file:
            csv_file = csv.writer(file)
            # csv_file.writerow(header)
            for data in datas:
                csv_file.writerow(data)
            file.close()
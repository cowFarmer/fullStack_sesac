from gen.generator import GeneratorData
import csv

class WriterData(GeneratorData):
    def write_data(self, count, category):
        datas = self.generate_data(count, category)
        header, save_file_name = self.category_header_file_name(category)

        with open("./save/" + save_file_name, "w", newline="\n") as file:
            csv_file = csv.writer(file)
            csv_file.writerow(header)
            for line in datas:
                csv_file.writerow(line)
            file.close()
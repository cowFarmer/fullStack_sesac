from gen.generator import GeneratorData

class PrinterData(GeneratorData):
    def print_data(self, count, category):
        datas = self.generate_data(count, category)
        header, _ = self.category_header_file_name(category)
        
        print(header)
        for data in datas:
            print(data)
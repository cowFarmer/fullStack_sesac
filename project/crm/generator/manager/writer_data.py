import csv


class WriterData:
    def __init__(self):
        self.category_header = {
            "user": ["Id","Name","Gender","Age","Birthday","Address"],
            "store": ["Id","Name","Type","Address"],
            "item": ["Id","Name","Type","UnitPrice"],
            "order": ["Id", "OrderAt", "StoreId", "UserId"],
            "orderitem": ["Id", "OrderId", "ItemId"]
        }
        
    def write_data(self, data, category):
        with open("./save/" + category + ".csv", "w", newline="\n") as file:
            csv_file = csv.writer(file)
            
            if category in self.category_header:
                header = self.category_header[category]
                csv_file.writerow(header)
            for d in data:
                csv_file.writerow(d)
            file.close()
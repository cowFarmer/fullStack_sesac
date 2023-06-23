from manager.checker_input_type import CheckerInputType
from manager.writer_data import WriterData
from manager.printer_data import PrinterData
from gen.generator import GenerateUser, GenerateStore, GenerateItem

def generate_user(count):
    users = []
    header = ["UUID","Name","Gender","Age","Birthday","Address"]
    users.append(header)
    for _ in range(count):
        user = GenerateUser().generate()
        users.append(user)
    return users

def generate_store(count):
    stores = []
    header = ["UUID","Name","Type","Address"]
    stores.append(header)
    for _ in range(count):
        store = GenerateStore().generate()
        stores.append(store)
    return stores

def generate_item(count):
    items = []
    header = ["UUID","Name","Type","UnitPrice"]
    items.append(header)
    for _ in range(count):
        item = GenerateItem().generate()
        items.append(item)
    return items


def main():
    gen_types = ["user", "store", "item"]
    output_type = ["console", "csv"]
    
    # checker, printer, writer    
    checker = CheckerInputType()
    data_category = checker.category_list(gen_types)
    count_generate_items = checker.count_generate_items()
    input_type = checker.input_type(output_type)
    
    printer = PrinterData()
    writer = WriterData()
    
    if data_category == "user":
        data = generate_user(count_generate_items)
        file_name = "person_data.csv"
    elif data_category == "store":
        data = generate_store(count_generate_items)
        file_name = "store_data.csv"
    elif data_category == "item":
        data = generate_item(count_generate_items)
        file_name = "item_data.csv"
        
    if input_type == "console":
        printer.print_data(data, data_category)
    elif input_type == "csv":
        writer.write_data(data, file_name, data_category)

if __name__ == "__main__":
    main()
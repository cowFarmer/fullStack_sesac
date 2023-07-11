from manager.checker_input_type import CheckerInputType
from manager.writer_data import WriterData
from manager.printer_data import PrinterData
from gen.generator import GenerateUser, GenerateStore, GenerateItem

def generate_user(count):
    users = []
    header = ["Id","Name","Gender","Age","Birthday","Address"]
    users.append(header)
    for _ in range(count):
        user = GenerateUser().generate()
        users.append(user)
    return users

def generate_store(count):
    stores = []
    header = ["Id","Name","Type","Address"]
    stores.append(header)
    for _ in range(count):
        store = GenerateStore().generate()
        stores.append(store)
    return stores

def generate_item(count):
    items = []
    header = ["Id","Name","Type","UnitPrice"]
    items.append(header)
    for _ in range(count):
        item = GenerateItem().generate()
        items.append(item)
    return items


def main():
    generate_type = ["user", "store", "item"]
    output_type = ["console", "csv"]
    
    # checker, printer, writer    
    checker = CheckerInputType()
    data_category = checker.category_list(generate_type)
    count_generate_items = checker.count_generate_items()
    input_type = checker.input_type(output_type)
    
    printer = PrinterData()
    writer = WriterData()
    # TODO 레지스터
    # 객체 저장하고 배열 만들어주는 나, 자신 처리할 수 있게끔
    # 팩토리, 빌드업 패턴 알아보기
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
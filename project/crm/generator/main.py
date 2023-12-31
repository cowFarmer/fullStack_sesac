from manager.checker_input_type import CheckerInputType
from manager.writer_data import WriterData
from manager.printer_data import PrinterData
from gen.factory import DataClient


def main():
    generate_type = ["user", "store", "item", "order", "orderitem"]
    output_type = ["console", "csv"]
    
    # checker, printer, writer    
    checker = CheckerInputType()
    data_category = checker.category_list(generate_type)
    count = checker.count_generate_items()
    result_type = checker.check_output_type(output_type)
    
    printer = PrinterData()
    writer = WriterData()
    client = DataClient()
    data = client.data_generate(data_category, count)
    
    if data_category == "item":
        unique = []
        set_data = []
        for d in data:
            name = d[1]
            if name not in unique:
                unique.append(name)
                set_data.append(d)
        data = set_data
    
    if result_type == "console":
        printer.print_data(data)
    elif result_type == "csv":
        writer.write_data(data, data_category)
    
    
if __name__ == "__main__":
    main()
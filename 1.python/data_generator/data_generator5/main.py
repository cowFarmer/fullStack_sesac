from manager.checker_input_type import CheckerInputType
from manager.writer_data import WriterData
from manager.printer_data import PrinterData

def main():
    checker = CheckerInputType()
    data_category = checker.category_list()
    count_generate_items = checker.count_generate_items()
    input_type = checker.input_type()
    writer = WriterData()
    printer = PrinterData()
    
    if input_type == "console":
        printer.print_data(count_generate_items, data_category)
    elif input_type == "csv":
        writer.write_data(count_generate_items, data_category)

if __name__ == "__main__":
    main()
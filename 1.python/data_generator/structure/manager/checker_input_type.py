class CheckerInputType:
    # 데이터 유형
    def category_list(self):
        category_list = ["user", "store", "item"]
        while True:
            data_category = input("데이터 유형을 입력하세요 'User', 'Store' or 'Item': ")
            if data_category.lower() in category_list:
                data_category = data_category.lower()
                break
            else:
                print("데이터 유형을 알맞게 입력하세요 'User', 'Store' or 'Item': ")
        return data_category
    
    # 데이터 개수
    def count_generate_items(self):
        while True:
            try:
                count_generate_items = abs(int(input("생성할 데이터 개수를 입력하세요: ")))
                break
            except ValueError:
                print("생성할 데이터 개수를 숫자로 입력하세요: ")
        return count_generate_items
    
    # 데이터 아웃풋 타입
    def input_type(self):
        input_type_list = ["console", "csv"]
        while True:
            input_type = input("출력 타입을 입력하세요 'console', 'csv': ")
            if input_type.lower() in input_type_list:
                break
            else:
                print("출력 타입을 알맞게 입력하세요 'console', 'csv': ")
        return input_type
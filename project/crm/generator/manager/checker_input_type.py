class CheckerInputType:
    # 데이터 유형
    def category_list(self, gen_types):
        category_list = gen_types
        while True:
            data_category = input(f"데이터 유형을 입력하세요 {category_list}: ")
            if data_category.lower() in category_list:
                data_category = data_category.lower()
                break
            else:
                print(f"데이터 유형을 알맞게 입력하세요 {category_list}: ")
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
    def check_output_type(self, output_type):
        input_type_list = output_type
        while True:
            input_type = input(f"출력 타입을 입력하세요 {input_type_list}: ")
            if input_type.lower() in input_type_list:
                break
            else:
                print(f"출력 타입을 알맞게 입력하세요 {input_type_list}: ")
        return input_type
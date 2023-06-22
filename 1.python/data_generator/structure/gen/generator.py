from gen.generate_name import GenerateName
from gen.generate_birthday import GenerateBirthday
from gen.generate_gender import GenerateGender
from gen.generate_address import GenerateAddress
from gen.generate_store import GenerateStore
from gen.generate_age import GenerateAge
from gen.generate_store_name import GenerateStoreName

class GeneratorData:
    def __init__(self):
        self.gen_name = GenerateName()
        self.gen_birthday = GenerateBirthday()
        self.gen_gender = GenerateGender()
        self.gen_address = GenerateAddress()
        self.gen_store_name = GenerateStore()
        
    ### TODO: 수정 필요
    def generate_data(self, count, category):
        datas = []
        for _ in range(count):
            address = self.gen_address.get_address()
            if category == "user":
                name = self.gen_name.get_name()
                birthday = self.gen_birthday.get_birthday()
                age = GenerateAge(birthday).get_age()
                gender = self.gen_gender.get_gender()
                datas.append([name, gender, age, birthday, address])
            if category == "store":
                store_name = self.gen_store_name.get_name()
                store_type = GenerateStoreName(store_name).get_type()
                datas.append([store_name, store_type, address])
        return datas
    
    def category_header_file_name(self, category):
        user_file_name = "person_data.csv"
        cafe_file_name = "cafe_data.csv"
        item_file_name = "item_data.csv"
        
        if category == "user":
            return ["Name", "Gender", "Age", "Birthday", "Address"], user_file_name
        elif category == "store":
            return ["Name", "Type", "Address"], cafe_file_name
        elif category == "item":
            return ["Name", "Type", "UnitPrice"], item_file_name
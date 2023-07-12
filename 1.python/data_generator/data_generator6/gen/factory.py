from abc import ABC, abstractmethod

from gen.generator import GenerateUser, GenerateStore, GenerateItem


# data generator 팩토리 패턴
class DataGeneratorFactory(ABC):
    @abstractmethod
    def generate(self):
        pass

class ConcreteUser(DataGeneratorFactory):
    def generate(self):
        user = GenerateUser().generate()
        return user

class ConcreteStore(DataGeneratorFactory):
    def generate(self):
        store = GenerateStore().generate()
        return store

class ConcreteItem(DataGeneratorFactory):
    def generate(self):
        item = GenerateItem().generate()
        return item

# 생성자
class DataCreator:
    def __init__(self):
        self.item_list = []
        
    def data_category(self, category: str):
        if category == "user":
            return ConcreteUser()
        elif category == "store":
            return ConcreteStore()
        elif category == "item":
            return ConcreteItem()
        else:
            raise ValueError("data_category를 확인해 주세요")

# 요청자
class DataClient:
    def __init__(self):
        self.data_list = []

    def data_generate(self, category: str, count=1):
        creator = DataCreator()
        category = creator.data_category(category)
        for _ in range(count):
            result = category.generate()
            self.data_list.append(result)
        return self.data_list
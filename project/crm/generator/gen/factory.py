from abc import ABC, abstractmethod

from gen.generator import GenerateUser, GenerateStore, GenerateItem, GenerateOrder, GenerateOrderItem


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

class ConcreteOrder(DataGeneratorFactory):
    def generate(self):
        order = GenerateOrder().generate()
        return order

class ConcreteOrderItem(DataGeneratorFactory):
    def generate(self):
        order_item = GenerateOrderItem().generate()
        return order_item

# 생성자
class DataCreator:
    def __init__(self):
        self.category_map = {
            "user": ConcreteUser(),
            "store": ConcreteStore(),
            "item": ConcreteItem(),
            "order": ConcreteOrder(),
            "orderitem": ConcreteOrderItem()
        }
        
    def data_category(self, category: str):
        if category in self.category_map:
            return self.category_map[category]
        else:
            raise ValueError("DataCreator를 확인해 주세요")

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
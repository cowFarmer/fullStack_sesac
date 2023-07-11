from abc import ABC, abstractmethod

from gen.generator import GenerateUser, GenerateStore, GenerateItem


# data generator 팩토리 패턴
class DataGeneratorFactory(ABC):
    @abstractmethod
    def generate(self):
        pass

# TODO: header 위치 변경
# 데이터 요청자가 카테고리, 개수 말하면
# 생성자가 카테고리에 맞는 data_list
# factory에서 생성만 하기
# header는 팩토리 패턴에서 하지 않기
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
        self.generate_type = ["user", "store", "item"]
        
    def data_category(self, input_type: str, count):
        if input_type == "user":
            return ConcreteUser()
        elif input_type == "store":
            return ConcreteStore()
        elif input_type == "item":
            return ConcreteItem()
        else:
            raise ValueError("category를 확인해 주세요")

# 요청자
class DataClient:
    def __init__(self, creator):
        self.creator = creator

    def request(self, category: str, count: int):
        category = creator.data_category()
        result = category.generate()
        print(result)

creator = DataCreator()
client = DataClient()
client.request()



class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Invalid shape type")

# 팩토리를 사용하여 도형 생성
factory = ShapeFactory()
circle = factory.create_shape("circle")
circle.draw()  # 출력: Drawing a circle

rectangle = factory.create_shape("rectangle")
rectangle.draw()  # 출력: Drawing a rectangle














from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Invalid shape type")

# 팩토리를 사용하여 도형 생성
factory = ShapeFactory()
circle = factory.create_shape("circle")
circle.draw()  # 출력: Drawing a circle

rectangle = factory.create_shape("rectangle")
rectangle.draw()  # 출력: Drawing a rectangle

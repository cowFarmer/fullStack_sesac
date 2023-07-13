import random

from gen.user.generate_name import GenerateName
from gen.user.generate_birthday import GenerateBirthday
from gen.user.generate_gender import GenerateGender
from gen.user.generate_age import GenerateAge
from gen.store.generate_store_name import GenerateStoreName
from gen.store.generate_store_type import GenerateStoreType
from gen.item.generate_item import GenerateItemInfo
from gen.order.generate_order_at import GenerateOrderAt

from gen.common.generate_address import GenerateAddress
from gen.common.generate_uuid import GenerateUuid
from gen.common.get_uuid import GetUuid


class GenerateUser:
    def __init__(self):
        self.gen_uuid = GenerateUuid()
        self.gen_name = GenerateName()
        self.gen_birthday = GenerateBirthday()
        self.gen_gender = GenerateGender()
        self.gen_address = GenerateAddress()
    
    def generate(self):
        uuid = self.gen_uuid.get_uuid()
        name = self.gen_name.get_name()
        birthday = self.gen_birthday.get_birthday()
        age = GenerateAge(birthday).get_age()
        gender = self.gen_gender.get_gender()
        address = self.gen_address.get_address()
        return [uuid, name, gender, age, birthday, address]
    
class GenerateStore:
    def __init__(self):
        self.gen_uuid = GenerateUuid()
        self.gen_store_name = GenerateStoreName()
        self.gen_address = GenerateAddress()
        
    def generate(self):
        uuid = self.gen_uuid.get_uuid()
        store_name = self.gen_store_name.get_name()
        store_type = GenerateStoreType(store_name).get_type()
        address = self.gen_address.get_address()
        return [uuid, store_name, store_type, address]
    
class GenerateItem:
    def __init__(self):
        self.gen_uuid = GenerateUuid()
        self.gen_item = GenerateItemInfo()
    
    def generate(self):
        uuid = self.gen_uuid.get_uuid()
        item_name = self.gen_item.get_item_name()
        item_type = self.gen_item.get_item_type(item_name)
        item_price = self.gen_item.get_item_price(item_name)
        return [uuid, item_name, item_type, item_price]
    
class GenerateOrder:
    _instance = None
    store_uuid = None
    user_uuid = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.get_uuid = GetUuid()
            cls.store_uuid = cls.get_uuid.get_uuid_from_data("store", "Id")
            cls.user_uuid = cls.get_uuid.get_uuid_from_data("user", "Id")
        return cls._instance
            
    def __init__(self):
        self.gen_uuid = GenerateUuid()
        self.gen_order_at = GenerateOrderAt()
    
    def generate(self):
        uuid = self.gen_uuid.get_uuid()
        order_at = self.gen_order_at.get_order_at()
        get_store_uuid = random.choice(self.store_uuid)
        get_user_uuid = random.choice(self.user_uuid)
        return [uuid, order_at, get_store_uuid, get_user_uuid]
    
class GenerateOrderItem:
    _instance = None
    order_uuid = None
    item_uuid = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.get_uuid = GetUuid()
            cls.item_uuid = cls.get_uuid.get_uuid_from_data("item", "Id")
            cls.order_uuid = cls.get_uuid.get_uuid_from_data("order", "Id")
        return cls._instance

    def __init__(self):
        self.gen_uuid = GenerateUuid()
        
    def generate(self):
        uuid = self.gen_uuid.get_uuid()
        order_uuid = random.choice(self.order_uuid)
        item_uuid = random.choice(self.item_uuid)
        return [uuid, order_uuid, item_uuid]
class Singleton:
    _instance = None
    print("1")
    @staticmethod
    def get_instance():
        print("2")
        print(Singleton())
        print(Singleton._instance)
        if Singleton._instance is None:
            print("3")
            Singleton._instance = Singleton()
        print("4")
        return Singleton._instance

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(id(s1))
print(id(s2))

#Singleton design pattern



class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = DBConnection()
b = DBConnection()
c = DBConnection()

print(a._instance) #without new method , the both objects are different
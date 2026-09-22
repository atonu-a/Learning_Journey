"""#Singleton design pattern



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
"""

# Factory Design pattern
class Car :
    def drive(self):
        return "driving a car"

class Bike:
    def drive(self):
        return "riding a bike"


class Vehicle:
    @staticmethod
    def get_info(type):
        if type=="car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return "Error"
        

v1 = Vehicle.get_info('car')
print(v1.drive())
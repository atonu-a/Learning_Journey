# Composition 
#It's a strong relationship. A class can't event exists without another

class Engine:
    def __init__(self, power) -> None:
        self.power = power
        
class Car:
    def __init__(self, name) -> None:
        self.name = name
        self.engine = Engine("800HP")
    def show_info(self):
        print(f"Car name : {self.name}\nPower : {self.engine.power}")
        
        
car1 = Car("Audi")
car1.show_info()
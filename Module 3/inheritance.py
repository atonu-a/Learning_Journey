"""# Single inheritance
class GrandFather:
    def __init__(self,name, title) -> None:
        self.name = name
        self.title  = title
        
        
class Father(GrandFather):
    def __init__(self, hobby, name, title):
        super().__init__(name, title)
        self.hobby = hobby


    
grand_f = GrandFather("Sunil", "Roy Chowdhury")   
father = Father("Fishing", "Sumon", grand_f.title )
print(father.name)
print(father.title)
print(father.hobby)
print(grand_f.name)
print(grand_f.title)"""


"""class Vehicle:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        
    def show_info(self):
        print(f"Brand : {self.brand}\nModel : {self.model}")
        
class Car(Vehicle):
    def __init__(self, model,  brand,number_of_doors):
        super().__init__(model, brand)
        self.number_of_doors = number_of_doors
        
    def show_car_info(self):
        print(f"Brand : {self.brand}\nModel : {self.model}\nNumber of Doors: {self.number_of_doors}")



car = Car("Corolla","Toyota",  4)

car.show_info()
car.show_car_info()"""
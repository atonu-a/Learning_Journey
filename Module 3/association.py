#Association
#Association means one clss can access another class's instances. An object can use another object as it's paremeter. It's an strong relationship
class Mobile:
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model


class Person:
    def __init__(self, name, phone) :
        self.name = name
        self.phone = phone
        
    def show_info(self):
        print(f"{self.name} has a {self.phone.brand} {self.phone.model} phone")


phone1 = Mobile("Samsung", "S24")
p1 = Person("Atonu", phone1)

p1.show_info()
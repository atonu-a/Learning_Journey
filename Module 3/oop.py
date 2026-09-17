class Phone:
    def __init__(self, brand, model) : #Parameterized Constructor
        self.brand = brand
        self.model = model
        
    def __init__(self, brand="Apple" , model ="18"):#Default Parameter
        self.brand = brand
        self.model = model
    

phone1 = Phone("Oppo", "S6")

phone2 = Phone(brand="Samsung", model="S26")

phone3 = Phone()
print(phone1.brand)
print(phone2.brand)
print(phone3.brand)

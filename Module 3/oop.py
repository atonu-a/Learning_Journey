class Phone:
    def __init__(self, brand, model) : #Parameterized Constructor
        self.brand = brand
        self.model = model
        
    def __init__(self, brand="Apple" , model ="18"):#Default Value Constructor
        self.brand = brand
        self.model = model
        
    def get_info(self): #Instance method
        print(f"Brand : {self.brand}\nModel : {self.model}")
    

phone1 = Phone("Oppo", "S6")

phone2 = Phone(brand="Samsung", model="S26")

phone3 = Phone()
phone1.get_info()
phone2.get_info()
phone3.get_info()

class Student : #Class
    def __init__(self, n, roll): #__init__() eta holo mainly constructor
        self.name = n
        self.roll = roll
    
    def say_hi(self):
        print(f"Hi {self.name}") #instance method
        
a = Student("Atonu", 734432)
a.say_hi()
print(a.roll)
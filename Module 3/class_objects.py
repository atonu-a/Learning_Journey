# Class is a blueprint template that is used to create objects
#Objects are instance or implementation of classes

class Student : #Class
    batch = 24 # it's a class variable
    
    @classmethod #eita use korle class er method update hobe kintu baire theke object diye kora jabe na
    def change(cls):
        cls.batch = 100
    def set_name(self, n):
        self.name = n
    
    def say_hi(self):
        print(f"Hi {self.name}") #instance method

# Student1 e self hisabe class e pass hocche


student1 =Student() #object
student1.set_name("Atonu")
b=Student()
# student1.name = "Atonu" #name = attribute/instance variable

student1.say_hi()
student1.change()
b.change()
b.batch = 10
print(b.batch)
print(student1.batch)

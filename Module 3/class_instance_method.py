class Employee:
    company = "AS"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def get_info(self): #instance method
        print(f"Employee Name : {self.name}\nCompany : {self.company} \nSalary : {self.salary}")
    
    
    @classmethod  
    def change_company(cls, company): #class method
        cls.company = company
        
        
e1 = Employee("Atonu", 18000)
e1.company ="Garena" # shudhu e1 er jonno change hobe
e1.get_info()

e2 = Employee("Afrina", 20000)
e2.change_company("ABC") #porer sobgulor jonnoi change hobe
e2.get_info()


e3 = Employee("Likhon", 20000)
e3.get_info()


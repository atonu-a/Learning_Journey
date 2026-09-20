class School:
    school_name = "ABC School"
    
    def info(self, name, roll): #It's an instance method, it's related to object. Every object can be different value, but static method will be same for every object
        self.name =  name
        self.roll = roll
    
    @staticmethod
    def calculate_grade(marks): #This is a common method. We dont need to pass cls or slef to call this, because it's not related to any object.
        if marks>=80:
            return "A+"
        else:
            return "A"
        
print(School.calculate_grade(89))
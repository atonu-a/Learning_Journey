class Student:
    section = "A" #Class Variable
    
    def __init__(self, name):
        self.student_name = name # Instance variable
        
        
st1 = Student("Atonu")
s2 = Student("Roton")
s2.section = "B" #Just ei object er jonno variable ta change hoyche


print(s2.section)
print(s2.student_name)
print(st1.section)
print(st1.student_name)
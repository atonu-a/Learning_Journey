#In Aggreration, the classes could be separate, we can use them together or indivisually. If we dont call the add_depts() then they can be separated.It is not mandatory to use an object as another object's parameter
class Department:
    def __init__(self, name) -> None:
        self.name = name
    

class University:
    def __init__(self, name) -> None:
        self.name = name
        self.depts = []
        
    def add_depts(self, dept):
        self.depts.append(dept)
    def show_depts(self):
        return [dept.name for dept in self.depts]
    
    
du = University("DU")
dept1 = Department("TCT")
dept2 = Department("CSE")
dept3 = Department("EEE")
du.add_depts(dept1)
du.add_depts(dept2)
du.add_depts(dept3)
du.add_depts(Department("ME"))
print(du.show_depts())
        
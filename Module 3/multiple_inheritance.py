class Father:
    def __init__(self, title) -> None:
        self.title = title
        
    def father_method(self):
        print("I've the characteristics from my father!")
class Mother:
    def __init__(self, habit) -> None:
        self.habit = habit
    def mother_method(self):
        print("I've the characteristics from my mother!")
        
class Child(Father, Mother):
    
    def __init__(self, name):
        self.name = name
    
    def child_method(self):
        print("I've the characteristics from both of my father and mother!")
        
        
child1 = Child("Atonu")
child1.father_method()
child1.mother_method()
child1.child_method()
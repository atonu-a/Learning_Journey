class Father:
    def father_method(self):
        print("I've the characteristics from my father!")
class Mother:
    def mother_method(self):
        print("I've the characteristics from my mother!")
        
class Child(Father, Mother):
    def child_method(self):
        print("I've the characteristics from both of my father and mother!")
        
        
child1 = Child()
child1.father_method()
child1.mother_method()
child1.child_method()
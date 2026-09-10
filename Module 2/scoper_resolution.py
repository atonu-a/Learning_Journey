"""LEGB
L -> Local
E -> Enclosing
G -> Global
B -> Built in Scope"""

x = 10 #global variable
print(x)
def outer_func():
    y= 10 # Enclosing variable
    print(y) 
    def inner_func():
        z = 100 #local variable
    
    
n = "global"

def outer2():
    n="enclosing"
    def inner2():
        # global n # eta shudhu global variable er value ke change korte parbe, local parbe na 
        
        nonlocal n # eta nonlocal ba enclosing variable ke change korte oare
        n="local"
        
        
        print(n)
    inner2()
outer2()
print(n)
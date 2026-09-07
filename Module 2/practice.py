# User defined functions
# 1. No input, no return

def first_function():
    print("this is my first function")
    
first_function()

# 2. Input, no return
def addition(a, b): #arguments
    print(a+b)
    
addition(10,15) #parameters

# 3. Input and return

def multiplication(a, b):
    return a*b

result = multiplication(10, 20)
print(result)

# 4. No input, return

def greetings():
    return "Hello"
print(greetings())

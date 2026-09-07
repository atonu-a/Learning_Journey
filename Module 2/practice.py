# # User defined functions
# # 1. No input, no return

# def first_function():
#     print("this is my first function")
    
# first_function()

# # 2. Input, no return
# def addition(a, b): #parameters
#     print(a+b)
    
# addition(10,15) #arguments

# # 3. Input and return

# def multiplication(a, b):
#     return a*b

# result = multiplication(10, 20)
# print(result)

# # 4. No input, return

# def greetings():
#     return "Hello"
# print(greetings())

# def sum(a, b):
#     res = a+b
# print(sum)
# print(sum(10,15))

calc = lambda a, b : a+b

print(calc(10, 20))
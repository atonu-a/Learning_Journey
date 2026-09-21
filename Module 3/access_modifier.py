class Example:
    public_var = "I am public" #Can be accessed from everywhere
    _protected_var = "I am protected" # Can be accessed from class and subclass
    __private_var = "I am private" #Can only be accessed from the class


a = Example()
print(a.public_var)
print(a._protected_var)
print(a.__private_var) #Cant access
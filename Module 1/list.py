"""a = [1, 10, 23, 24, 26, 90]

# To calculate length of a list
print(len(a)) #6

# Append in list
a.append(100)
print(a) #[1, 10, 23, 24, 26, 90, 100]

# Clear list
print(a.clear()) #None

# Convert a string into a list

s = "Hello"
print(list(s)) #['H', 'e', 'l', 'l', 'o']"""
   

# Range method
# range (start, end, step)
# range(end)
# range (start, end)

a = list(range(10)) # range(end)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = list(range(1, 10))
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

a = list(range(0, 10, 2))
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# {}
# {"key" : "value"}
# no indexing
# Keys are immutable

a = {
    'rahim': 12,
    'karim' : 27
}

for i in a : # the loop is iterating on the keys in the dictionary
    print(i) # prints only the keys not the values

print("----")
for i in a.values(): # the loop is iterating over the values of the dictionary
    print(i) # now it can print the values
    

print("----")

print(a.keys()) #dict_keys(['rahim', 'karim'])
print(a.values()) #dict_keys(['rahim', 'karim'])


print("----")


# Printing keys and values together
for key, val in a.items():
    print(f"{key} : {val}")

print(a.items()) #dict_items([('rahim', 12), ('karim', 27)])
print("----")

list1 = [1, 2,3]
list2 = [ "Apple", "Mango", "Banana"]

dict1 = dict(zip(list1, list2)) # zip function makes pair from 2 list

print(dict1) #{1: 'Apple', 2: 'Mango', 3: 'Banana'}

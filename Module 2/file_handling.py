# file = open('Module 2/name.txt', 'w')
# content = file.write("")
# print(content)

# file.close()


"""# It overwrites the previous file
with open('Module 2/name.txt', 'w') as file:
    content = file.write("My name is Atonu Roy Chowdhury")

with open('Module 2/name.txt', 'r') as file:
    content = file.read()
    print(content)
    """
    
    
"""#Writting file without overwritting
with open("Module 2/name.txt", 'a') as file:
    content = file.write("\nAdding a new text statement.")"""
    


# adding multiple things using list in file   
lines = ["Line 1", "Line 2", "Line 3"]


#With Looping
for line in lines:
    with open("Module 2/name.txt", 'a') as file:
        content = file.write(f"\n{line}")

#Real strategy
with open("Module 2/name.txt", 'a') as file:
    content = file.writelines(lines)


# File ekbar read hoye gele cursor sobar seshe chole ashe tai 2nd time ar pora jay na ejonno seek() method diye cursor e position fix kora jay

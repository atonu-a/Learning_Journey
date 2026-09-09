
import pathlib #File path checking kore
import os #Os e check kore


"""
if os.path.exists('name.txt'):
    print("File Exists")
else :
    print("Not Exists")
    
if os.path.exists('Module 2/name.txt'):
    print("File Exists")
else :
    print("Not Exists")
    """


file_path = pathlib.Path('Module 2/name.txt')

if file_path.exists():
    print("File Exists")
else :
    print("Not Exists")


print(os.path.abspath("Module 2/name.txt"))  #Absolute file path
print(os.path.getsize("Module 2/name.txt"))   
#file size in bytes

with open("Module 2/name.txt", "r") as f:
    print(f.tell()) #shows the cursor position of this file
with open("Module 2/name.txt", "r") as f:
    print(f.read(5)) #shows the 1st 5 character from this file
    
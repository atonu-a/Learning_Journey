"""try : #Prothome try korbe
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    div = a/b
    print(div)
except Exception as e: # try te kono error thakle eta asbe
    print(e)
else : #try te kono error na thakle eta run hobe
    print("Code executed successfully!") 
finally : # always eta run hobeiiiii
    print("Done")
    """
    
# Manually Error toiri ba raise kora
def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt files are accepted!") #Ekhane manuall vabe ekta error/exception raise kora holo. Ekhane jekono error deya jay chaile
    else:
        print("File uploaded successfully!")
        
check_file("name.txt")      
check_file("name.png")

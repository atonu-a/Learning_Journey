try : #Prothome try korbe
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
    
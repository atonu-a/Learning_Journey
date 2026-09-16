# Manually Error toiri ba raise kora
def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt files are accepted!") #Ekhane manuall vabe ekta error/exception raise kora holo. Ekhane jekono error deya jay chaile
    else:
        print("File uploaded successfully!")


file_name = "name.cshdfsgsdfgv"      
try :
    check_file(file_name) 
        
    
except ValueError:
    print("Only .txt files are accepted!")
try:
    f = open("namess.txt", 'r') #file is not available
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print(e)
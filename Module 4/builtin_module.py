# import math #Built in module

# print(math.floor(12.6))
# print(math.factorial(10))

import requests
html = requests.get("https://google.com").text

print()

with open("index.html" , "w") as file:
    content = file.write(html)
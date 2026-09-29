import requests
import json

# URL =  "https://dummyjson.com/posts"

# res = requests.get(URL)

# data = json.loads(res.text)

# print(data["posts"][0]["title"])

# Get request
URL = "https://jsonplaceholder.typicode.com/posts"

res = requests.get(URL)
data = res.json()[1]


# print(json.dumps(data,indent=4))

# with open("texts/output.txt", "w", encoding="utf-8") as f:
#     f.write(data)

# POST request
"""data2 = {
    "userId": 100000,
    "id": 2,
    "title": "for testing",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
}

res = requests.post(URL, data)
print(res.status_code)
print(res.json())"""

#Update request
"""data = {'userId' : 1, 'id':1, 'title': 'for testing(updated)'}

res = requests.put(f"{URL}/1", json=data)
print(res.status_code)
print(res.json())"""

#Delete request
res = requests.delete(f"{URL}/1", json=data)
print(res.status_code)
print(res.json())

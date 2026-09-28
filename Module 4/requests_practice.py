import requests
import json

URL =  "https://dummyjson.com/posts"

res = requests.get(URL)

data = json.loads(res.text)

print(data["posts"][0]["title"])
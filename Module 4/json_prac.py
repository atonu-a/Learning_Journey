import json

data = {
    'name' : "Rahim",
    'age' : 30,
    'is_logged_in': True
    
}

json_string = json.dumps(data, indent=4)
print(json_string)
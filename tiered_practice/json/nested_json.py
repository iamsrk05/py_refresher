import json
data = {
    "users": [
        {
            "id": 1,
            "name": "Sam",
            "skills": ["Python", "SQL"]
        },
        {
            "id": 2,
            "name": "Alex",
            "skills": ["Pandas", "NumPy"]
        }
    ]
}


with open("tiered_practice/json/user.json", "w") as file:
    json.dump(data, file, indent=4)
    
with open("tiered_practice/json/user.json", "r") as file:    
    loaded_data = json.load(file)
    
print(loaded_data)

print(loaded_data["users"])

for user in loaded_data["users"]:
    print(user["name"])
import json

data = {
    "users": [
        {
            "id": 1,
            "name": "Sam",
            "age": 22,
            "skills": ["Python", "SQL"]
        },
        {
            "id": 2,
            "name": "Alex",
            "age": 19,
            "skills": ["Pandas", "Python"]
        },
        {
            "id": 3,
            "name": "Mira",
            "age": 24,
            "skills": ["SQL", "NumPy"]
        }
    ]
}

with open("tiered_practice/json/users.json", "w") as file:
    json.dump(data, file, indent=4)

with open("tiered_practice/json/users.json", "r") as file:
    load_file = json.load(file)


for user in load_file["users"]:
    print(f"{user['name']} - {user['age']}")


unique_skills = set()

for user in load_file["users"]:
    unique_skills.update(user["skills"])

print(unique_skills)


age_map = {}

for user in load_file["users"]:
    age_map[user["name"]] = user["age"]

print(age_map)
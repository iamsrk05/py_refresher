import json

student = {
    "name": "Sam",
    "age": 22,
    "skills": ["Python", "SQL", "Pandas"]
}

json_data = json.dumps(student)
python_data = json.loads(json_data)

with open("tiered_practice/json/student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("tiered_practice/json/student.json", "r") as file:
    loaded_data = json.load(file)

print(json_data)
print(type(json_data))

print(python_data)
print(type(python_data))

print(loaded_data)
print(type(loaded_data))
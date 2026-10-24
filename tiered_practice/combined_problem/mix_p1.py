student_info = ("Sam", 22)

raw_skills = [
    "Python",
    "SQL",
    "Python",
    "Pandas",
    "SQL"
]

name, age = student_info

unique_skills = set(raw_skills)

unique_skills.add("NumPy")

student = {
    "name" : name,
    "age" : age,
    "skills" : unique_skills
}

print(student)

print(student["skills"])
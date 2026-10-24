student_scores = [
    ("Sam", 85),
    ("Alex", 92),
    ("Mira", 85),
    ("John", 70)
]

score_map = {}

for name, score in student_scores:
    score_map[name] = score
    
unique_scores = set()

for name, score in student_scores:
    unique_scores.add(score)
    
print(score_map)
print(unique_scores)

print(score_map["Alex"])
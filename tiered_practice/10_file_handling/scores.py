with open("tiered_practice/file_handling/scores.txt", "r") as file:
    lines = file.readlines()
    
print(lines)

scores = {}

for line in lines:
    cleaned_line = line.strip()
    parts = cleaned_line.split(",")
    
    name , score = parts
    score = int(score)
    scores[name] = score
    
    print(name,score)
    
print(scores)


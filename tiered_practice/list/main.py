# data = [10, 20, 30]

# data.append(40)
# data.insert(1, 99)
# data.remove(20)

# print(data)

# scores = [70, 85, 90, 85, 60]

# scores.append(95)
# scores.remove(85)
# scores.insert(1, 75)
# print(scores)
# name = scores.sort(reverse=True)
# name = scores.pop(1)
# print(name)


scores = [70, 85, 90, 85, 60]

scores.append(95)
scores.remove(85)
scores.insert(1, 75)

print(scores)

new_scores = scores.copy()
new_scores.sort(reverse=True)

new_scores.pop(1)

print(new_scores)

# square = lambda number: number ** 2

# print(square(5))


# add = lambda a, b: a + b

# print(add(10,20))

# check_result = lambda score: "Pass" if score > 50 else "Fail"

# print(check_result(38))
# print(check_result(74))



score = [39,45,45,75,83.52]

passed = list(filter(lambda score: score >= 50, score))

print(passed)
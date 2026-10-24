# class student:
#     name = "sam"
#     score = 85

# student1 = student()
# student2 = student()

# student1.name = "Rafi"
# student1.score = 34

# student2.name = "karim"
# student2.score = 54

# print(student1)
# print(student2)


# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# student1 = student("sam",85)

# print(student1)



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

emp1 = Employee("Alex", 5000)
emp2 = Employee("Sam", 7000)

emp1.increase_salary(1000)

print(emp1.salary)
print(emp2.salary)


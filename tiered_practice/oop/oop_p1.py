class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_bonus(self, bonus):
        self.score += bonus

    def check_result(self):
        if self.score >= 50:
            return "Pass"
        else:
            return "Fail"

student1 = Student("Rafi",33)            
student2 = Student("karim", 70)  

student1.add_bonus(10)   

print(f"{student1.name} : {student1.score} - {student1.check_result()} ")
print(f"{student2.name} : {student2.score} - {student2.check_result()} ")

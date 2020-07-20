

# class Tiger():

#     def __init__(self, name, age):
#         self.name = name
#         self.ag = age
#         print(f"I am {name}")
#         print(f'I am {age} Years Old!')

#     def addOne(self, a):
#         return a +10

#     def roar(self):
#         print("I roar very loud")
#         exit()
#     def get_name(self):
#         return self.name

# Tiger('Tom', '9')
# Tiger('Bill', 12)

class Profile():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        self.grade = ""
        if self.score >= 700:
            self.grade = "AAA"
        elif self.score >= 650:
            self.grade = "AA"
        else:
            self.grade = "A" #Either A, AA, or AAA
    def getGrade(self):
        return self.grade

class Course():
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []
    def addstudents(self, student):
        if len(self.students) < self.maxStudents:
            self.students.append(self.students)
            return True
        return False
    def getAverageGrade(self):
        value = 0
        for student in students:
            value += student.getGrade
        
        return value / len(self.student)

Student1 = Profile("Tom", 18, int(input('enter the Marks of Student1>')))
Student2 = Profile("Elliot", 19, int(input("Enter the marks of Student2>")))
Student3 = Profile("Harry", 20, int(input("Enter the marks os Student3>")))
print(Student1.getGrade())
# print(Student2.getGrade())
# print(Student3.getGrade())

course = Course("Science", 2)
# course.addstudents(Student1)
# course.addstudents(Student2)
print(course.getAverageGrade)
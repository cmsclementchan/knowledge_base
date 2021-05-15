# Object Oriented Programming in Python

class Student :
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # list

    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Tim",18,79)
s2 = Student("Clement",20,90)
s3 = Student('Kin',20,70)

course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)

# not able to add more student 
print(course.add_student(s3))

# cal the average 
print(course.get_average_grade())
class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = name[0] + last_name + birth_year


a_student = Student(input(), input(), input())
print(a_student.student_id)

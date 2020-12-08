class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = name[0] + last_name + birth_year


a_student = Student(input(), input(), input())
print(a_student.student_id)


"""
Students
John works at the university. He deals with the information about a lot of students and he decided to 
create a program that would help him with it.

He devised a system for creating an id for each student: first letter of the name, last name, 
and then the birth year. For example, the id for John Smith (b. 1989) would look like JSmith1989.

John needs help finishing the code for the id and then applying it to the students. 
Your task is to define an instance attribute student_id in the __init__ method, calculate it, 
create an object of the class Student with the parameters from the input, and print the value 
of the id. Do NOT print the value inside of the __init__ method!

The input format:

Student information: the first line has the name, the second line has the last name, 
and the third has the birth year.

The output format:

The student_id of the student.

NOTE: the attribute names are case sensitive, so check that the attribute is named exactly student_id.
Other names lead to an AttributeError!

Sample Input:
Daniel
Smith
1993
Sample Output:
DSmith1993

Sample Input:
Katherine
Fell
1997
Sample Output:
KFell1997

Caution
You may see errors in your code or execution results due to missing context. 
Don’t worry about it, just write the solution and press Check.
"""
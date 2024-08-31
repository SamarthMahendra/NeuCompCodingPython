"""
Question: Imagine you are in a school, and you want to ask your friend's friend about homework. Do you think it's better to ask your friend to talk to their friend for you, or should you just go directly to your friend's friend?

Answer Choice:
a) Ask your friend to ask their friend.
b) Go directly to your friend's friend.

ans b) Go directly to your friend's friend.
When you ask your friend to talk to their friend for you, it's like playing a game of telephone.
 The message might get mixed up, and it takes longer. It's much simpler to talk directly to the person you need.
"""



## bad practice
class Student:

    def __init__(self, name):
        self.name = name


class Classroom:

    def __init__(self, student):
        self.student = student


class School:

    def __init__(self, classroom):
        self.classroom = classroom

    def print_student_name(self):
        print(self.classroom.student.name)

st =  Student("samarth")
cl = Classroom(st)
sh = School(cl)
sh.print_student_name()


## good practice

class Student:

    def __init__(self, name):
        self.name = name



class Classroom:

    def __init__(self, student):
        self.student = student

    def get_student_name(self):
        return self.student.name


class School:

    def __init__(self, classroom):
        self.classroom = classroom

    def print_student_name(self):
        print(self.classroom.get_student_name())

st =  Student("samarth")
cl = Classroom(st)
sh = School(cl)
sh.print_student_name()



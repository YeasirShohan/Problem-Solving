# OOP
# task1 Non static method
#WAP to create a class that define the avarage of 3 mark.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum=0
        for i in self.marks:
            sum += i
        print("Hello", self.name, "your avarage mark is", sum/3)

s1 = Student(str(input("Enter your name: ")),
             [int(input("Enter Your 1st marks")),
              int(input("Enter Your 2st marks")),
              int(input("Enter Your 3st marks"))])
s1.avg()
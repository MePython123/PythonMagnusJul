class Teacher:
    def english(self):
        print("English Language")
class Student1(Teacher):
    def math(self):
        print("Math Subject")
class Student2(Teacher):
    pass
obj1 = Student1()
obj2 = Student2()
obj1.english()
obj1.math()
obj2.english()

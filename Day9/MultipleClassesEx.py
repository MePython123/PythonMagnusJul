class Sample:
    def m1(self):
        print("Welcome M1 Function")
class Demo(Sample):
    def m2(self):
        print("Welcome M2 Function")
obj1 = Demo()
obj1.m1()
obj1.m2()
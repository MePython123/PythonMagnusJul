class Sample:
    a = 10
    b = 20
    def m1(self):
        print("M1 Function")
obj = Sample() # creating an object for class
print(obj.a)
obj.m1()
print(type(obj))
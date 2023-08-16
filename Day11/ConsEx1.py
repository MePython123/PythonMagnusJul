class Sample:
    def m1(self):
        print("M1 function")
    def m2(self):
        print("M2 function")
    def __int__(self,a,b):
        print(a+b)
obj1 = Sample()
obj1.m1()
obj1.m2()
class Sample:
    def m1(self):
        a=10
        b=0
        try:
            print(a/b)
            print(c)
        except ZeroDivisionError as e:
            print("Don't Provide the Denominator Value as Zero")
        except NameError as e1:
            print(e1)
        except Exception as e2:
            print(e2)
        try:
            print(c)
        except NameError as e:
            print(e)
obj1 = Sample()
obj1.m1()
print("End of the Program")
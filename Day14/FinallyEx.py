class Sample:
    def m1(self):
        a=10
        b=10
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print(e)
        finally:
            print("Zero Division Done")

    def m2(self):
        c=10
        try:
            print(c)
        except NameError as e:
            print(e)
        finally:
            print("Name Error Done")

obj1 = Sample()
obj1.m1()
obj1.m2()
class GrandParent:
    def a1(self):
        print("2 Assets")
class Parent(GrandParent):
    def a2(self):
        print("3 Assets")
class Son(Parent):
    def a3(self):
        print("1 Asset")
obj1 = Son()
obj2 = Parent()
obj1.a1()
obj1.a2()
obj1.a3()
obj2.a2()
obj2.a1()


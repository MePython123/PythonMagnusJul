class Father:
    def home(self):
        print("2 flats and 2 plots with house")
class Mother:
    def car(self):
        print("2 cars")
    def cash(self):
        print("1Billion cash")
class Son(Father, Mother):
    pass
obj1 = Son()
obj1.home()
obj1.car()
obj1.cash()
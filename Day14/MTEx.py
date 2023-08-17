from threading import Thread
from time import sleep
class Sample(Thread):
    def m1(self):
        for i in range(1,21):
            print(i)
            sleep(1)
    def m3(self):
        print("m3")
    def run(self):
        self.m1()
        self.m3()
class Demo(Thread):
    def run(self):
        for i in range(21,41):
            print(i)
            sleep(1)

obj1 = Sample()
obj2 = Demo()
obj1.start()
obj2.start()
obj1.join()
print("End of the Program")
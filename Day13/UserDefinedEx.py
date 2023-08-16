class EligibleError(Exception):
    pass
class Sample:
    def eligible(self,age,percentage):
        if age<18 or percentage<60:
            raise EligibleError("Not Eligible for Registration")
        else:
            print("Registration Success")

obj1 = Sample()
obj1.eligible(17,70)
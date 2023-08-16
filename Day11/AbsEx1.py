from abc import ABC,abstractmethod
class Accounts:
    def savings(self):
        print("No Min Balance and Earn upto 7.5% monthly Int")

class Loans(ABC):
    @abstractmethod
    def pl(self):
        print("personal Loan")
    @abstractmethod
    def hl(self):
        print("House Lone")

class FinalAccount(Accounts,Loans):
    def pl(self):
        print("Persoanl Loan")
    def hl(self):
        print("Home loan with 8% Floating Int")

obj1 = FinalAccount()
obj1.savings()
obj1.pl()
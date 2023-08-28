"""Write a program that reads two numbers A and B, and checks if sum of squares of A
and B is greater than or equals to 60."""

a=int(input("Enter the Value of a: "))
b=int(input("Enter the Value of b: "))
c=(a**2)+(b**2)
if c>60:
    print(" is Greater")
else:
    print(" is Lesser")
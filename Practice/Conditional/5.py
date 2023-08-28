"""Give three angles of a triangle, write a program to check whether the triangle is valid
or not."""

a=int(input("Enter the Value of A: "))
b=int(input("Enter the Value of B: "))
c=int(input("Enter the Value of C: "))
t = a+b+c
if t==180:
    print("It is a Valid Triangle")
else:
    print("Not a Triangle")
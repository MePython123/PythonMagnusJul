"""Write a Program that read a number N and checks if the last digit of N is equal to the
last digit of the square of N"""


a=int(input("Enter the Value of a: "))
b=a**2
c=str(a)
d=str(b)
e=len(c)-1
f=len(d)-1
if c[e]==d[f]:
    print("Equal")
else:
    print("Not Equal")
"""Write a program to read N inputs and print a list containing the first and
last three inputs."""
a=int(input("Enter the List Count of Values: "))
l = []
for i in range(a):
    b=input("Enter the Value into a List: ")
    l.append(b)
print(l)
print(l[:3]+l[-3:])
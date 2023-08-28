"""Create a list, Given a number N, write a program that prints the list by
repeating the List N times."""
L = [10,20,45,'abc']
j=[]
a=int(input("Enter the Count of Values: "))
for i in range(a):
    j+=L
print(j)
"""Given a number N , write a program that read N numbers and prints a list
of numbers that are divisible by 5."""
n=int(input("Enter the Count of Values: "))
l = []
outlist = []
for i in range(n):
    l.append(int(input("Enter the Value in a List: ")))
for j in l:
    if j%5==0:
        outlist.append(j)
print(l)
print(outlist)

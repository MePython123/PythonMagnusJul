"""A List L is given in 4. the prefilled code.
L = ["apple", "78", "970.03"]
Given a number N , write a program that reads N inputs and prints the list
by adding a given N inputs at the end of the list L."""
L = ["apple", "78", "970.03"]
a=int(input("Enter the Count of Values: "))
for i in range(a):
    b=input("Enter the Value in a List: ")
    L.append(b)
print(L)

"""Write a program that reads a two-digit number N and cheks if any of the given
conditions is satisfied
a.The sum of digits of N is equal to 7
b. One of the digits of N is equal to 7
c. N is divisible by 7
d. Print "Special Number if any of the given conditions is satisfied. Otherwise, print
'Normal Number'"""


digit = int(input("Enter the two Digit Number: "))
a=str(digit)
b=int(a[0])+int(a[1])
if b==7 or a[0]==7 or a[1]==7 or (digit%7)==0:
    print("Special Number")
else:
    print("Not a Special Number")
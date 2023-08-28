"""Write a Program that reads the scores A and B of two players and checks if one of the
scores is greater than 300 and the sum of the scores is less than 500. Print 'Can Team
Up' if one the scores is greater than 300 and the sum of the scores is less than 500,
otherwise print 'Cannot Team Up' """

a = int(input("Enter the Value of A: "))
b = int(input("Enter the Value of B: "))
c=a+b
if (a>300 or b>300) and c<500:
    print("Can Team Up")
else:
    print("Cannot Team Up")
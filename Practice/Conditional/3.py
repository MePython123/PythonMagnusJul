"""Write a Program that reads a temperature and checks if the given temperature is
between 15 and 40. print 'Can go for a Walk' if it is between 15 and 40."""
a=int(input("Enter the temp Value: "))
if a>15 and a<40:
    print("Can go for a Walk")
else:
    print("Cannot go for a walk")
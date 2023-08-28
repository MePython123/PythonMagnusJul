"""A company decided to give a bonus of 5% to an employee if his/her years of service is
more than five years. Write a program that reads an employee's salary and years of
service and decides whether the employee gets the bonus or not."""
service = int(input("Enter the Service Count: "))
salary = int(input("Enter the Salary: "))
if service>5:
    print(salary*(5/100))
else:
    print("No Bonus")
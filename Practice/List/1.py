"""1.a=['Python', 'Java', 'Ruby', 'Move', 'C++', 'Go', 'C', 'R', 'Swift', 'perl']
Input:
The first line of input will contain a positive integer(N)
The following N lines will contain a positive number in each line.
Explanation:
If the given number is 2, read the inputs in the next two lines and print the
elements at the given indexes. If the given two indexes are 1 and 4"""

a=['Python', 'Java', 'Ruby', 'Move', 'C++', 'Go', 'C', 'R', 'Swift', 'perl']
b=int(input("Enter the First Integer Number N:"))
for i in range(b):
    c=int(input("Enter the Index Position to Print:"))
    print(a[c])

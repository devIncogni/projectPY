# for loop in python
# Program to print from a to b integers
# For Loop iterates over iterable objects in Python

name = "ArinKumar"
for i in name:
    if i=="a" or i=="A":
        print("LESS GOOO")
        continue
    print(i)

color = ['red','green','blue','yellow','orange','violet']
for i in color:
    for j in i:
        print(j)
    print(i)

for i in range(5):
    print (i)

a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
c=int(input("Enter step number "))

for i in range(a,b+1,c):
    print(i)
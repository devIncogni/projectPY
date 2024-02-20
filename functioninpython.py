# Functions in Python

def gmean(a,b):
    return a*b/(a+b)

def isGreater(a,b):
    if(a>b):return a
    else: return b

def laterFunction():
    pass


a,b=5,4

print(str(gmean(a,b)) + " Greater Number: " + str(isGreater(a,b)))

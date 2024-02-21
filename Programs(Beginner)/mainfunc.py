import time

def patternKBC(m=4):
    for i in range(1,m):
        print ("KK", end="")
        for j in range (m,0,-1):
            if j==i: print(' KK', end='')
            else: print(" ", end='')
        time.sleep(0.5)
        print()

    for i in range(1,m+1):
        print ("KK", end="")
        for j in range (1,m+2):
            if j==i: print(' KK', end='')
            else: print(" ", end='')
        time.sleep(0.5)
        print()

patternKBC()

while(True):
    a=input("Enter a number")
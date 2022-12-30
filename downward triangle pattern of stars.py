# pattern 17.
n=int(input("Range : "))
print("Pattern #17: Downward Triangle Pattern of Stars")
for i in range(n+1,0,-1):
    for j in range(n+1-i):
        print("",end=" ")
    for j in range(i+i,i,-1):
        print("*",end=" ")
    print()
print()
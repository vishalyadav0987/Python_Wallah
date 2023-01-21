# pattern 18.
n=int(input("Range : "))
print("Pattern #18: Pyramid Pattern of Stars")
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print()
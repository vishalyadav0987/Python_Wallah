# pattern 2.
n=int(input("Range : "))
print("Pattern #2: Inverted Pyramid of Numbers")
for i in range(n,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()   
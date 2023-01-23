# pattern 16.
# print("Pattern #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers")
n=int(input("Range : "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")        
    for j in range(i,i+i):
        print("*",end=" ")   
    print()     
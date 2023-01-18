# pattern 15.
n=int(input("Range : "))
print("Pattern #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers")
for i in range(n):
    for j in range(n-i):
        print("",end=" ")
    for j in range(i+1,0,-1):       
        print(j,end=" ")
    print() 

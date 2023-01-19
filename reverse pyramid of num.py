# # pattern 6.
n=int(input("Range : "))
print("Pattern #6: Reverse Pyramid of Numbers")
for i in range(0,n):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()   
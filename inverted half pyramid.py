# # pattern 7.
print("Pattern #7: Inverted Half Pyramid Number ")
n=int(input("Range : "))
for i in range(-1,n):
    for j in range(0,n-i):
        print(j,end=" ")
    print()    

n=int(input("Range : "))
# # pattern 1.
print("Pattern #1: Simple Number Triangle Pattern")
for i in range(1,n):
    for j in range(i,i+i):
        print(i,end=" ")
    print()    

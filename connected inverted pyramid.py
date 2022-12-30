# # pattern 11.
n=int(input("Range : "))
print("Pattern #11: Connected Inverted Pyramid ")
for i in range(1,n):
    for j in range(n-1,i-1,-1):
        print(j,end=" ")
    for j in range(i,n):
        print(j,end=" ")    
    print()    

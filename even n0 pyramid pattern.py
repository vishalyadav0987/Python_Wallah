# # pattern 12.
n=int(input("Range : "))
print("Pattern #12: Even Number Pyramid Pattern")
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j*2,end=" ")   
    print()    

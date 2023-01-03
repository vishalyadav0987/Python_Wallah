# # pattern 3.
print("Pattern #3: Half Pyramid Pattern of Numbers")
n=int(input("Range : "))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

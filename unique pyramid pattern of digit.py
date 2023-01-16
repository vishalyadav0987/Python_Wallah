# # # pattern 10.
n=int(input("Range : "))
print("Pattern #10: Unique Pyramid Pattern of Digits")
for i in range(0,n):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()    
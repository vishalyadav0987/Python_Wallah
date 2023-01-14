# # pattern 4.
n=int(input("Range : "))
print("Pattern #4: Inverted Pyramid of Descending ")
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print() 

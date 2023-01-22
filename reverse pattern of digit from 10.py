# # pattern 9
n=int(input("Range : "))
print("Pattern #9: Reverse Pattern of Digits from 10 ")  
a=0
for i in range(1,n):
    for j in range(a+i,a,-1):
        print(j,end=" ")
        a+=1
    print()   

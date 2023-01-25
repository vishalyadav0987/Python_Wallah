# question 6:
a=int(input("how many to give input : "))
l=[]
for i in range(a):
    i=int(input("number: "))
    l.append(i)
print(l)
for j in l:
    if j>0:
        print(j,"is postive integer")       
    elif j<0:
        print(j,"is negative integer")
    if j==0: 
        print(j,"is not defined")   
    elif j%2==0 :
        print(j,"is even number")    
    elif j%2!=0:
        print(j,"is odd number") 
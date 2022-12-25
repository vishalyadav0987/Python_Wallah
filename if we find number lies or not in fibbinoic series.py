L=[]
for i in range(int(input("How many digits you type:--"))):
    i=int(input("--"))
    L.append(i)
hi=max(L)
# print(L)
x=int(hi)
a=0
b=1
z=0
l=[]
if x<0:
    print("only gives postive values")
elif x==1:
    print(a)
else:
    while z<x:
        l.append(a)
        p=a+b
        a=b
        b=p
        z=z+1
    # print(l)
         
    length=len(L)
    for j in range(length):
        if L[j] in l:
            print("valid",L[j])
        elif L[j] not in l:
            print("invalid",L[j]) 
        else:
            print("this number is not exsist")    
               
           
                    

        



     

    
     
    
          
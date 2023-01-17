x=int(input("wants to no's of fibanoic series:---"))
a=0
b=1
z=0
l=[]
if x<=0:
    print("only gives postive values")
elif x==1:
    print(a)
else:
    while z<x:
        l.append(a)
        A=a+b
        a=b
        b=A
        
       
        z=z+1
    print(l)     
       
    
       

    

    


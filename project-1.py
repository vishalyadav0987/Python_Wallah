i=0
L=[]
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
    # import random   
    # e=random.choice(l)  
    # print(e)
    
while True:
     for i in range(int(input("How many digits you type:--"))):
        i=int(input("--"))
        # import random
        L.append(i)
     
    #  d=random.choice(L)
    #  print(d)
     if l in L :
        print("you are winner")
     else:
         print("you are loser") 
          
         
    

        
    
               
     
     
     
   
     
     

    # a,b=input("Enter single aur couples of number:--- ").split()
   

     
    

    
    
        
    
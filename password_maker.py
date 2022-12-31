print("THE MINIMUM LENGTH OF PASSWORD IS 12")
user=int(input("ENTER THE LENGTH OF PASSWORD : "))
rem=user%4
if user<12:
    print("THE MINIMUM LENGTH OF PASSWORD IS 12")   
else:
    f=user//4
    import random as r
    l1=[]
    b=["A","B","S","D","F","G","H","J","K","L","Q","W","E","R","T","Y","U","I","O","Z","X","C","V","B","N","M"]
    for i in range(f+rem):
        y=r.choice(b)
        l1.append(y)
    d=["a","s","d","f","g","h","h","j","k","l","z","x","c","v","b","n","m","q","w","e","r","t","y","u","i","o"]
    for i in range(f):
        W=r.choice(d)
        l1.append(W)
    c=["!","@","#","$","%","^","&","*"]
    for i in range(f):
        z=r.choice(c)
        l1.append(z)
    a=[1,2,3,4,5,6,7,8,9,0]
    for i in range(f):
        x=r.choice(a)
        l1.append(x)
    if user<12:
        print("THE MINIMUM LENGTH OF PASSWORD IS 12")
    else:
        print(l1)
        s=r.shuffle(l1)
        for j in l1:
            print(j,end="")





    






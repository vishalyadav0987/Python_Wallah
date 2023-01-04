print(
'''for play say's
        Y     or    N   ''')
print()
s="YOU ARE WINNER!!!!!"

while True:
    USER=input("ENTER FOR_PLAY SAY Y OR N : ")
    if USER=="Y" or USER=="y":
        R1=int(input("ENTER YOUR STARTING RANGE : "))
        R2=int(input("ENTER YOUR ENDING RANGE : "))
        l=[]
        for i in range(R1,R2):
            l.append(i)
        import random as r
        z=r.choice(l)
        l1=[]
        for j in range(1,4):
            j=int(input("ENTER YOUR GUESSING NUMBER : "))
            if z<j:
                print("YOUR GUESSING IS TOO HIGH")
                continue
            elif z>j:
                print("YOUR GUESSING IS TOO LOW")
                continue
            else:
                print( s,"==",z)
                break
        sum=""
        l2=[]
        if "YOU ARE WINNER!!!!!":
            sum+=s
            l2.append(sum)
        print(l2)   
    else:
        print("BETTER LUCK NEXT TIME!!!!")
        break

#print("1,2,4,5,11,12")



    
    

    




    

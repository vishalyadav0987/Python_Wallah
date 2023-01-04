
z=0
print('''for play say's
        Y     or    N   ''')
while True:
   
    for_play=input("you want to play:----")
    if for_play=="y" or for_play=="Y":
        import random
        x=int(input("take no from the user(1,6):---"))
        p=random.randint(1,6)
        print("Robot choosed by no. own mind:---",p)
        if p==x:
            print("Yeah!! you are winner")
        elif p!=x:
            print("Btter Luck Next Time:lose the game!")
    else:
        print("Ok Play Next Time")  
        break        
             
        
    
        


      
        
    
       
    

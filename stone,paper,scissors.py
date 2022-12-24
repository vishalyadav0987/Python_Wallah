a=["Rock","Paper","Scissors"]
i=0
while True:
    for_play=input("do you want play:--")
    
    if for_play=="Y" or for_play=="y":
        user=input("user chosed in a:-- ") 
       
        import random
        pc=random.choice(a)
        print(pc)
        if pc==user:
            print("Congurulation! you are winner")
        else:
            print("Better Luck For Next Time") 
    else:
        print("go back home and study")        
        break
          
    
     
     
    
    



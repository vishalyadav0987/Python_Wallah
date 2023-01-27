print('''TAP FOR CONVERTING RUPEE..
        1. POUNDS
        2. EUROS 
        3. US DOLLAR
        4. CANADIAN DOLLAR
        5. CHINESE YUAN
        6. RUSSIAN'S RUBEL ''')
user=int(input("ENETER YOUR CURRENCY IN RUPEES : " ))
TAP = input("WHAT DO YOU WANT TO CONVERT : ")
if TAP=="1":
    print(user,"Rupees in","{:.2f}".format(user/100.11),"Pound")
elif TAP=="2":
    print(user,"Rupees in","{:.2f}".format(user/88.76),"Euros")
elif TAP=="3":
    print(user,"Rupees in","{:.2f}".format(user/82.75),"Us dollar")  
elif TAP=="4":
    print(user,"Rupees in","{:.2f}".format(user/60.98),"Canadian dollar")  
elif TAP=="5":
    print(user,"Rupees in","{:.2f}".format(user/12),"Chinese yen")
elif TAP=="6":
    print(user,"Rupees in","{:.2f}".format(user/1.12),"Russian's rubel")
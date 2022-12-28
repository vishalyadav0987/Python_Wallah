print('''Add +
         substract -
         division /
         multiplication *
         ''')
num1=int(input("num1: "))
num2=int(input("num2: "))       
oprator=input("enter your opr:....(+,-,/,*)")

if oprator=="+":
    print(num1+num2)
elif oprator=="-":
    print(num1-num2)
elif oprator=="/":
    print(num1/num2)
elif oprator=="*":
    print(num1*num2)            
else:
    print("invalid oprator")    






A=int(input("Type your Range starting from : "))
B=int(input("Type your Range last from : "))
l=[]
for i in range(A,B):
    l.append(i)
import random
Rno=random.choice(l)
print(Rno)
# Rno=int(input("cvvvb : "))
if int(Rno)<0:
    print(int(Rno),"is NEGATIVE number")
elif int(Rno)>0:
    print(int(Rno),"is POSTIVE number")    
if int(Rno)%2==0:
    print(int(Rno),"is EVEN number")
else:
    print(int(Rno),"is Odd number") 
if int(Rno)>1:
        for i in range(2,Rno):
            if int(Rno)%i==0:
                print(int(Rno),"is  COMPOSITE number")
                break
        else:
            print(Rno,"is  PRIME number") 
     
else:
    print(int(Rno),"is NOR PRIME or NOR COMPOSITE")    







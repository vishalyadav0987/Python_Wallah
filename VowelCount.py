a=input("Enter your String : ")
l=["a","i","e","o","u"]
con=0
vol=0
def count():
    for i in a:
        if i in l:
            con=con+1
    else:
        vol=vol+1        
count()            

k=""
for i in a:
    if i not in k:
        k+=i
for i in k:
    print(i,a.count(i))  
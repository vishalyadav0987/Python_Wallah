a=int(input())
b=str(a)
s=0
for i in b:
    s+=(int(i))**len(b)
print(s)
if(s==a):
    print("armstrg no")
else:
    print("not")
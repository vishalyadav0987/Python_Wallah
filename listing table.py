l = list(map(int,input().split()))
l1 = []
l2=["2","3","7","5"]
c = 0
for i in l:
    if i%2==0:
        c = c+1
l1.append(c)
c1=0
for i in l:
    if i%3==0:
        c1 = c1+1
l1.append(c1) 
c2=0
for i in l:
    if i%7==0:
        c2 = c2+1
l1.append(c2)               
c3=0
for i in l:
    if i%5==0:
        c3 = c3+1
l1.append(c3) 
l4=dict(zip(l2,l1))
print(l4)
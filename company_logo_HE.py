s=input()
l1=[]
for j in s:
    l1.append(j)
    l1.sort()
r=sorted(l1,key=l1.count,reverse=True)


l = []
[l.append(x) for x in r if x not in l]
y=[]
for i in l:
    d=l1.count(i)
    y.append(d)
m=[]
n=[]
for k in l:
    if (r.count(k))>=(int(y[2])):
        m.append(k)
        n.append(r.count(k))

for o in range(3):
    print(m[o],n[o])
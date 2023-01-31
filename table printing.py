l =[]
while True:
    a = input()
    if a=="stop" and a=="STOP":
        break
    else:
        l.append(int(a))
print(l)
b = int(input())
if b in l:
    sum = 0
    for j in range(1,11):
        sum+=b*j
print(sum)
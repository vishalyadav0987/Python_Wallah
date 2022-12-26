a=int(input("Type your Range starting from : "))
b=int(input("Type your Range last from : "))
for i in range(1,9):
    c=i**3
    if a<c<b:
        print(c)
        break
else:
    print("error")   
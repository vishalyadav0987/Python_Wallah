import random
def myfunc(a,b):
    c=random.randint(a,b)
    for i in range(3):
        a=int(input("Guess the random number: "))
        if a>c:
            print("Have one more try, Your guess was too high")
        elif a<c:
            print("Have one more try, Your guess was too small")
        elif a==c:
            print("Congrat's, You guessed this in {} attempt".format(i+1))
            break
    else:
        print("Better luck next time")
a=int(input("Enter a number for range: "))
b=int(input("Enter a number for range: "))
myfunc(a,b)
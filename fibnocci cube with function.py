cube = lambda x:x**3 
def fibonacci(n):
    l = []
    a = 0
    b = 1
    if n==0:
        pass
    elif n==1:
        l.append(a)
    else:
        l.append(a)
        l.append(b)
        for i in range(2,n):
            A = a+b
            a=b
            b=A
            l.append(A)
    return l            

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
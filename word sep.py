def split_and_join(line):
    a=line.split()
    l=[]
    for i in range(len(a)):
        if i!=len(a)-1:
            l.append(a[i])
            l.append("-")
        else:
            l.append(a[-1])
    c="".join(l)
    return c 
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
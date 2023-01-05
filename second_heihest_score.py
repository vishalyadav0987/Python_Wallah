if __name__ == '__main__':
    # n = int(input())
    arr = list(map(int, input().split()))
    b=set(arr)
    score = list(b)
    score.sort()
    print(score[-2])
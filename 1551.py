def number(n) :
    m = list(map(int, input().split()))
    f = int(input())
    for i in range(len(m)) :
        if m[i] == f :
            return i + 1
    return -1
n = int(input())
print(number(n))
n, b = map(int, input().split())
a = [] ; c = 1
for i in range(n):
    aa = []
    for j in range(b):
        aa.append(0)
    a.append(aa)
for m in range(b):
    i = b - 1 - m
    if m % 2 == 0:
        for j in range(n):
            a[j][i] = c
            c += 1
    else:
        for j in range(n-1, -1, -1):
            a[j][i] = c
            c += 1
for i in a:
    print(*i)
n = int(input())
a = [] ; c = 1
for i in range(n) :
    aa = []
    for j in range(i + 1) :
        aa.append(0)
    a.append(aa)
for i in range(n - 1, -1, -1) :
    for j in range(len(a[i])-1, -1, -1) :
        a[i][j] = c
        c += 1
for i in range(n) :
    print(*a[i])
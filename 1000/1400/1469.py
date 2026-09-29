n = int(input())
a = [] ; c = 1
for i in range(n) :
    aa = []
    for j in range(n) :
        aa.append(0)
    a.append(aa)
for i in range(n) :
    if i % 2 == 0 :
        for j in range(n - 1, - 1, - 1) :
            a[i][j] = c
            c += 1
    else :
        for j in range(n) :
            a[i][j] = c
            c += 1
for i in range(n) :
    print(*a[i])
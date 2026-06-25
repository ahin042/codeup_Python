m,mm = map(int,input().split())
c = m * mm ; a = []
for i in range(m) :
    aa = []
    for j in range(mm) :
        aa.append(0)
    a.append(aa)
for i in range(mm) :
    for j  in range(m) :
        a[j][i] = c
        c -= 1
for i in range(m) :
    print(*a[i])
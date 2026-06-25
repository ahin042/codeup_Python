a,b = map(int,input().split())
aaa = [] ; m = a * b
for i in range(a) :
    aa = []
    for j in range(b) :
        aa.append(0)
    aaa.append(aa)
for i in range(a) :
    for j in range(b - 1, -1, -1) :
        aaa[i][j] = m
        m -=   1
for i in range(a) :
    print(*aaa[i])
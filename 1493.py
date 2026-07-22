a,b = map(int,input().split())
n = [] ; m = []
for i in range(a) :
    n.append(list(map(int,input().split())))
for i in range(a) :
    mm = []
    for j in range(b) :
        mm.append(0)
    m.append(mm)
x = 0 ; y = 0
for i in range(a) :
    for j in range(b) :
        for x in range(i + 1) :
            for y in range(j + 1) :
                m[i][j] += n[x][y]
for i in range(a) :
    print(*m[i])
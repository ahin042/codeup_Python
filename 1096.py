a = [] ; n = []
for i in range(19) :
    aa = []
    for j in range(19) :
        aa.append(0)
    a.append(aa)
for i in range(int(input())) :
    n.append(list(map(int, input().split())))
for i in n :
    a[i[0] - 1][i[1] - 1] = 1
for i in a :
    print(*i)
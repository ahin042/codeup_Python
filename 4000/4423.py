a = []
for i in range(101) :
    aa = []
    for j in range(101) :
        aa.append(0)
    a.append(aa)
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            a[x][y] = 1
c = 0
for i in range(101) :
    for j in range(101) :
        if a[i][j] == 1 :
            c += 1
print(c)
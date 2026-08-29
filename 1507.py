import sys as s

c = []
for i in range(100) :
    a =[]
    for j in range(100) :
        a.append(0)
    c.append(a)
for i in range(4):
    x1, y1, x2, y2 = map(int, s.stdin.readline().split())
    sx, ex = min(x1, x2), max(x1, x2)
    sy, ey = min(y1, y2), max(y1, y2)
    for x in range(sx, ex):
        for y in range(sy, ey):
            c[x][y] = 1
t = sum(sum(i) for i in c)
print(t)
n = int(input())
a = [] ; c = 1
for i in range(n) :
    aa = []
    for j in range(n) :
        aa.append(0)
    a.append(aa)
for i in range(n) :
    for j in range(n) :
        a[j][i] = c
        c += 1
c = 0
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            c += a[i][j]
print(c)
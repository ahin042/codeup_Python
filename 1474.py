n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
c = 1
for j in range(m - 1, -1, -1):
    if (m - 1 - j) % 2 == 0:
        for i in range(n - 1, -1, -1):
            a[i][j] = c
            c += 1
    else:
        for i in range(n):
            a[i][j] = c
            c += 1

for i in a:
    print(*i)
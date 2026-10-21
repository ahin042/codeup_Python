n = int(input())
a = [[0] * n for i in range(n)]
r = 0
c = n // 2
a[r][c] = 1
for b in range(2, n * n + 1):
    m = r - 1
    k = c + 1
    if m < 0:
        m = n - 1
    if k == n:
        k = 0
    if a[m][k] != 0:
        m = r + 1
        k = c
    r = m
    c = k
    a[r][c] = b
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
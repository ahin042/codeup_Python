n = int(input())
m = [[0] * n for i in range(n)]
for i in range(n):
    a = int(input())
    m[i][0] = a
    for j in range(1, i + 1):
        m[i][j] = m[i][j - 1] - m[i - 1][j - 1]
for i in range(n):
    r = ''
    for j in range(i + 1):
        r += str(m[i][j]) + ' '
    print(r)
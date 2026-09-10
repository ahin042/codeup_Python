a = [[0] * 100 for i in range(100)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            a[y + i][x + j] = 1
r = 0
b = [0] * 100
for i in range(100):
    for j in range(100):
        b[j] = b[j] + 1 if a[i][j] == 1 else 0
    s = []
    for j in range(101):
        h = b[j] if j < 100 else 0
        while s and b[s[-1]] >= h:
            m = b[s.pop()]
            w = j if not s else j - s[-1] - 1
            r = max(r, m * w)
        s.append(j)
print(r)
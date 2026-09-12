n = int(input())
m = [[0] * n for _ in range(n)]
a = 1; t = 0; b = n - 1 ; l = 0 ;  r = n - 1
while t <= b and l <= r:
    for c in range(l, r + 1):
        m[t][c] = a
        a += 1
    t += 1
    for i in range(t, b + 1):
        m[i][r] = a
        a += 1
    r -= 1
    if t <= b:
        for c in range(r, l - 1, -1):
            m[b][c] = a
            a += 1
        b -= 1
    if l <= r:
        for i in range(b, t - 1, -1):
            m[i][l] = a
            a += 1
        l += 1
for i in m:
    print(' '.join(map(str, i)))
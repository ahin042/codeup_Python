a = []
for i in range(5):
    r = list(map(int, input().split()))
    a.append(r)
b = []
for i in range(5):
    r = list(map(int, input().split()))
    for j in range(5):
        b.append(r[j])
m = []
for i in range(5):
    r = []
    for j in range(5):
        r.append(False)
    m.append(r)
n = 0
for i in range(25):
    num = b[i]
    for j in range(5):
        for k in range(5):
            if a[j][k] == num:
                m[j][k] = True
    c = 0
    for j in range(5):
        if m[j][0] and m[j][1] and m[j][2] and m[j][3] and m[j][4]:
            c += 1
    for j in range(5):
        if m[0][j] and m[1][j] and m[2][j] and m[3][j] and m[4][j]:
            c += 1
    if m[0][0] and m[1][1] and m[2][2] and m[3][3] and m[4][4]:
        c += 1
    if m[0][4] and m[1][3] and m[2][2] and m[3][1] and m[4][0]:
        c += 1
    if c >= 3:
        n = i + 1
        break
print(n)
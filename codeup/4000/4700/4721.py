n = int(input())
m = {
    1: [0, 0, 0],
    2: [0, 0, 0],
    3: [0, 0, 0]
}
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(3):
        x = j + 1
        s = a[j]
        m[x][0] += s
        if s == 3:
            m[x][1] += 1
        elif s == 2:
            m[x][2] += 1
r = []
for i, j in m.items():
    r.append([i, j[0], j[1], j[2]])
r.sort(key=lambda x: (-x[1], -x[2], -x[3]))
a = r[0]
s = r[1]
if a[1] == s[1] and a[2] == s[2] and a[3] == s[3]:
    print(0, a[1])
else:
    print(a[0], a[1])
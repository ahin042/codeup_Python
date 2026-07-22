n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
r = []
for i in range(n):
    count = 0
    for j in range(n):
        if a[j][0] > a[i][0] and a[j][1] > a[i][1]:
            count += 1
    r.append(count + 1)
print(*r)
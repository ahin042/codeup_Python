n = int(input())
m = {}
lst = []
for i in range(n):
    a = list(map(str, input().split()))
    m[a[0]] = float(a[1])
    lst.append(a[0])
n = sorted(m.values(), reverse = True)
r = {}
for i, j in enumerate(n):
    r[j] = i + 1
for i in lst:
    print(i, r[m[i]])
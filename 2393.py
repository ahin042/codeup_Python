n = int(input())
m = {}
lst = []
for i in range(n):
    a = list(map(str, input().split()))
    m[a[0]] = float(a[1])
    lst.append(a[0])
n = sorted(m.values(), reverse=True)
for i in lst:
    r = n.index(m[i]) + 1
    print(i, r)
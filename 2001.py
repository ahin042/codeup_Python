p = [] ; lst = []
for i in range(3):
    n = int(input())
    p.append(n)
m = p[0]
for i in range(2):
    n = int(input())
    lst.append(n)
for n in p:
    if n < m:
        m = n
r = lst[0]
for i in lst:
    if i < r:
        r = i
rt = (m + r) * 1.1
print(f"{rt:.1f}")
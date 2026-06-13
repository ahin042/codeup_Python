m = list(map(int, input().split()))
n = []
for i in range(len(m)):
    if m[i] % 2 == 0:
        n.append(m[i])
for i in n:
    m.remove(i)
if m == []:
    print(-1)
else :
    a = 0
    for i in m :
        a += i
    print(a)

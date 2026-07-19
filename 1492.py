a = int(input())
n = list(map(int, input().split()))
r = []
for i in range(a) :
    r.append(0)
for i in range(a) :
    for j in range(i + 1) :
        r[i] += n[j]
print(*r)
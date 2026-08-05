n = int(input())
a = list(map(int, input().split()))
i, j = map(int, input().split())
r = sum(a[i-1:j])
c = 0
for i in range(n):
    m = 0
    for b in range(i, n):
        m += a[b]
        if m == r:
            c += 1
print(c)
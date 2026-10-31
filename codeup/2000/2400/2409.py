n, k = map(int, input().split())
p = list(map(int, input().split()))
t = sum(p)
r = k - t
if r <= 0:
    print(-1)
else:
    print(r)
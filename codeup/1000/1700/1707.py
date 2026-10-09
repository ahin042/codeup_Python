a = list(map(int, input().split()))
c = sum(a) / 10
n = 0
m = 0
for i in a:
    if i >= c:
        n += 1
    else:
        m += 1
print(f"{c:.1f}")
print(n, m)
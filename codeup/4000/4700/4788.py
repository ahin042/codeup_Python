a = int(input())
b = list(map(int, input().split()))
c = [0] * a
n = 0
m = a - 1
while n < a:
    c[n] = b[n]
    n += 1
c.sort()
n = 0
while n < a:
    if c[n] != n + 1:
        print(-1)
        break
    n += 1
if n == a:
    print(a)
    print(*c)
a, b = map(int, input().split())
n = [[0] * b for _ in range(a)]
c = 1
for i in range(a + b - 1):
    m = min(i, a - 1)
    mm = i - m
    while m >= 0 and mm < b:
        n[m][mm] = c
        c += 1 ; m -= 1 ; mm += 1
for i in n :
    print(*i)
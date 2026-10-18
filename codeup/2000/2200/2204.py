a, b = map(int, input().split())
r = 0
for i in range(a, b + 1):
    for j in range(i, b + 1):
        n = i * j
        if str(n) == str(n)[::-1]:
            if n > r:
                r = n
print(r)
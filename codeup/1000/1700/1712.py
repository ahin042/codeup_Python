a, b, c = map(int, input().split())
d = b - a
i = a
while i <= c:
    print(i, end=' ')
    i += d
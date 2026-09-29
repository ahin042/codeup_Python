a,b = map(str, input().split())
a = int(a[:2]) ; b = int(b)
if b == 1:
    a += 1900
elif b == 2:
    a += 1900
elif b == 3:
    a += 2000
else :
    a += 2000
print(-1 * (a - 2012) + 1)
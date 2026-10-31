n = int(input())
r = 0
a = 1
b = 1
k = 1
for i in range(n):
    r += a
    b -= 1
    if b == 0:
        a *= 2
        k += 1
        b = k
print(r)
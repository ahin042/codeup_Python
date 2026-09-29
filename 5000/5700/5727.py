a = int(input())
b = int(input())
c1 = 0
c2 = 0
for i in range(10):
    c1 += a
    c2 += b
    a += 10
    b += 5
print(c1)
print(c2)
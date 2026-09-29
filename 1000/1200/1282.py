a = int(input())
c = 1
for i in range(a) :
    if c * c <= a and a < (c + 1) * (c + 1):
        break
    c += 1
r = a - c * c
print(r,c)
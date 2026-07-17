a,b = map(int, input().split())
r1 = 1 ; r2 = 1
for i in range(a, a - b, -1) :
    r1 *= i
for i in range(b, 0 , -1) :
    r2 *= i
print(r1 // r2)
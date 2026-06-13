a,b = map(int, input().split())
for i in range(a, - 1, - 1) :
    if a % i == 0 and b % i == 0:
        print(i)
        break
if a > b :
    a,b = b,a
for i in range(1,b + 1) :
    if (a * i) % b == 0:
        print(a * i)
        break
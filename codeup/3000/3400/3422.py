n = int(input())
r = 1
while n % 2 == 0:
    n //= 2
    r += 1
print(r)
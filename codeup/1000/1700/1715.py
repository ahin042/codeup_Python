import math as m

a, b = map(int, input().split())
g = m.gcd(a, b)
print(a // g, b // g)
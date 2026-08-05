def fun(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
mo = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28,
      31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28]
dt = []
for l in mo:
    for d in range(1, l + 1):
        dt.append(d)
n = int(input())
c = 1 ; p = 1 ; t = 1
while t < n:
    c += 1
    d = dt[c - 1]
    if fun(d):
        m = p * 3
    else:
        m = p * 2
    t += m
    p = m
print(c)
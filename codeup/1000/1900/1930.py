m = []
for i in range(15):
    m.append([0] * 15)
def fun(nn, n):
    if nn == 0:
        return n
    if m[nn][n] > 0:
        return m[nn][n]
    r = 0
    for i in range(1, n + 1):
        r += fun(nn - 1, i)
    m[nn][n] = r
    return r
while True:
    try:
        a = input().split()
        nn = int(a[0])
        n = int(a[1])
        print(fun(nn, n))
    except:
        break
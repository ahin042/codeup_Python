n = int(input())
a = [0] + list(map(int, input().split()))

r = (n + 1) // 2

def fun(k, c):
    c = c & a[k]
    m = k * 2
    if m > n:
        return c
    return fun(m, c) + fun(m + 1, c)

b = fun(1, 1)
print(r, b)
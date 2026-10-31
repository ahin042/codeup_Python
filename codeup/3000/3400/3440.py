def f(n, k, a):
    if k > n:
        return
    if n == 0:
        r.append(a)
        return
    f(n - 1, k, a + "0")
    if k > 0:
        f(n - 1, k - 1, a + "1")

n, k = map(int, input().split())
r = []
f(n, k, "")
print(" ".join(r))
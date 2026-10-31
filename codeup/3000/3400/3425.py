def f(n, a, b, c):
    if n == 0:
        return
    f(n - 1, a, b, c)
    r.append(str(n) + " : " + a + "->" + b)
    f(n - 1, c, b, a)
    r.append(str(n) + " : " + b + "->" + c)
    f(n - 1, a, b, c)

n = int(input())
r = []
f(n, "A", "B", "C")
r.append(str(3 ** n - 1))
print("\n".join(r))
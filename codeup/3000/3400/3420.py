def f(n, a, b, c):
    if n == 0:
        return
    f(n - 1, a, c, b)
    print("Disk", n, ":", a, "to", c)
    f(n - 1, b, a, c)
n = int(input())
f(n, "A", "B", "C")
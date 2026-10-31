def f(n, a, b, c):
    if n == 0:
        return
    f(n - 1, a, c, b)
    print("move disk", n, a + "->" + c)
    f(n - 1, b, a, c)

n = int(input())
print(2 ** n - 1)
f(n, "A", "B", "C")
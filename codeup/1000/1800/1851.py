def f(k):
    if k <= 0:
        return
    f(k - 1)
    print('*', end='')

n = int(input())
f(n)
print()
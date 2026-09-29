def m(n) :
    if n == 1:
        print(1)
        return 1
    elif n % 2 == 0:
        print(n)
        return m(n // 2)
    else:
        print(n)
        return m(3 * n + 1)
a = int(input())
m(a)
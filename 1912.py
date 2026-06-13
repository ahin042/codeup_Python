def p(n) :
    if n == 1:
        return 1
    return n * p(n - 1)
n = int(input())
print(p(n))
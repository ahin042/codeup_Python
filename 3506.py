n = int(input())
a = 1 ; b = 2
if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for i in range(3, n + 1):
        a, b = b, a + b
    print(b)
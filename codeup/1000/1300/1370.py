a, b = map(int, input().split())
for i in range(b):
    for j in range(a):
        print(' ' * j + '*')
    for j in range(a - 2, -1, -1):
        print(' ' * j + '*')
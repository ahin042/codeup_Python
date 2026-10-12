a, b = map(int, input().split())
for i in range(a, b + 1):
    n = str(i)
    c = n.count('3') + n.count('6') + n.count('9')
    if c > 0:
        print("K" * c)
    else:
        print(i)
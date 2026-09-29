a, b, c = map(int, input().split())
for i in range(c):
    n = input()
    r = ''
    for j in n:
        r += j * a
    for k in range(b):
        print(r)
a, b = map(int, input().split())
n = []
for i in range(a):
    n.append(input().split())
for i in n:
    print(*i)
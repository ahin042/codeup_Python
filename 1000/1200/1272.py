a,b = map(int, input().split())
n = [] ; c = max(a, b)
for i in range(1, c + 1) :
    n.append(i)
    n.append(i * 10)
print(n[a - 1] + n[b - 1])
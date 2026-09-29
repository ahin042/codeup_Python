a = []
for i in range(3) :
    m,n, = map(int, input().split())
    a.append(m * n)
print(max(a))
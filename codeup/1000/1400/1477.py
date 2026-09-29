a,b = map(int,input().split())
n = [] ; c = 1
for i in range(a) :
    nn = []
    for j in range(b) :
        nn.append(0)
    n.append(nn)
for d in range(a + b - 1):
    for i in range(a):
        j = d - i
        if 0 <= j < b:
            n[i][j] = c
            c += 1
for i in n:
    print(*i)
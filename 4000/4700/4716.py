c = 0 ; n = []
for i in range(10) :
    a,b = map(int,input().split())
    c += b
    c -= a
    n.append(c)
print(max(n))
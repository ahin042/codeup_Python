a,b = map(int,input().split())
n = list(map(int,input().split()))
r = [] ; c = []
for i in range(len(n)) :
    r.append(n[i])
    if len(r) == b :
        c.append(min(r))
        r = []
try :
    c.append(min(r))
    print(*c)
except ValueError :
    print(*c)
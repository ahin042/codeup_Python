k,m = map(int,input().split())
n = list(map(int,input().split()))
r = 0 ; c = 1
for i in n :
    if r + i > m :
        c += 1
        r = i
    else :
        r += i
print(c)
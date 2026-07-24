a = int(input())
n1 = 100 ; n2 = 100
for i in range(a) :
    c,c2 = map(int,input().split())
    if c > c2 :
        n2 -= c
    elif c < c2 :
        n1 -= c2
    else :
        continue
print(n1)
print(n2)
a,b,c = map(int,input().split())
i = 0
while i != c :
    i += 1
    a *= b
if b == 0 :
    print(0)
else :
    print(a // b)
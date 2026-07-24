a,b = map(int,input().split())
if a * b <= 200000 :
    print(a * b)
elif a * b > 200000 and a * b <= 500000 :
    print(int(a * b + (a * b - 200000) * 0.05))
else :
    print(int(a * b + (a * b - 200000) * 0.1))
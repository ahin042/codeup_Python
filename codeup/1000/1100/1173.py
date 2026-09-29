a,b = map(int,input().split())
if b - 30 >= 0 :
    print(a,b - 30)
else :
    if a - 1 >= 0 :
        print(a - 1,(60 + b) - 30)
    else :
        print(23,(60 + b) - 30)
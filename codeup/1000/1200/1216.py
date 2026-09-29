a,b,c = map(int,input().split())
if b - (a + c) > 0 :
    print("advertise")
elif b - (c + a) < 0 :
    print("do not advertise")
else :
    print("does not matter")
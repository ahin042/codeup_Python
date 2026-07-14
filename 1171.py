a,b,c = map(int,input().split())
a = str(a)
if b < 10 :
    b = "0" + str(b)
else :
    b = str(b)
if c < 10 :
    c = "00" + str(c)
elif c < 100 :
    c = "0" + str(c)
else :
    c = str(c)
print(a + b + c)
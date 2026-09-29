a = int(input())
r = 0
a = str(2012 - a + 1)
if int(a) < 2000 :
    r = 1
else :
    r = 3
a = int(a[2:])
print(a, r)

a = list(map(int,input().split()))
c = max(a)
a.remove(max(a))
if c < a[0] + a[1] :
    print("yes")
else :
    print("no")
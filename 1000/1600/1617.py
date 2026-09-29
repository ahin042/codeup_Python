n = str(input())
m = int(n) ; n = int(n[::-1])
a = str(m + n)
if a == a[::-1] :
    print("YES")
else :
    print("NO")
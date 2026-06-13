m = list(map(int, input().split()))
n1 = [] ; n2 = []
for i in m :
    if i % 2 == 1:
        n1.append(i)
    else:
        n2.append(i)
if n1 == [] :
    print(max(n2))
elif n2 == [] :
    print(min(n1))
else :
    print(max(n1) + max(n2))
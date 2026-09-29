m = list(map(int, input().split()))
a = [] ; b = []
for i in m :
    if i % 2 == 1:
        a.append(i)
    else:
        b.append(i)
if a != [] :
    print(max(a))
if b != [] :
    print(max(b))
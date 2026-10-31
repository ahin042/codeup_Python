m = int(input())
a = list(map(int, input().split()))
n = int(input())
c1 = []
c2 = []
c3 = []
for i in a:
    if i < n:
        c1.append(i)
    elif i == n:
        c2.append(i)
    else:
        c3.append(i)
r = c1 + c2 + c3
print(*r)

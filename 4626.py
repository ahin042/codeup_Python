a = int(input())
lst = list(map(int, input().split()))
c = 0
r = 1
for i in lst :
    if (i == 1) :
        c += r
        r += 1
    else :
        r = 1
print(c)
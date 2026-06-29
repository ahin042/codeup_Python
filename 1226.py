a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0 ; r = 0
for i in b:
    if i in a[:6]:
        c += 1
    if i == a[-1]:
        r += 1
if c == 6:
    print(1)
elif c == 5 and r == 1:
    print(2)
elif c == 5:
    print(3)
elif c == 4:
    print(4)
elif c == 3:
    print(5)
else:
    print(0)

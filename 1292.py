a = input()
r = 0
for i in range(len(a)) :
    r += int(a[i])
if r % 7 == 4 :
    print("suspect")
else :
    print("citizen")
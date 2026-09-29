m = input()
x = 0 ; n = []
for i in m :
    x += 1
    if i == "t" :
        n.append(x)
print(*n)
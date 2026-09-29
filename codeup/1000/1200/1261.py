n = list(map(int, input().split()))
r = 0
for i in n :
    if i % 5 == 0 :
        r = i
        break
print(r)
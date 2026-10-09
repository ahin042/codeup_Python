a = int(input())
b = list(map(int, input().split()))
for i in b:
    r = 1
    for j in b:
        if j > i:
            r += 1
    print(i, r)
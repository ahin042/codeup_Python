m = [list(map(int, input().split())) for i in range(5)]
c = 0
for i in range(3):
    for j in range(3):
        a = 0
        for r in range(i, i + 3):
            for k in range(j, j + 3):
                a += m[r][k]
        if a > c:
            c = a
print(c)
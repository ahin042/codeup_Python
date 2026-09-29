a = []
for i in range(100):
    aa = []
    for j in range(100):
        aa.append(0)
    a.append(aa)
n = int(input())
for i in range(n):
    m, mm = map(int, input().split())
    for j in range(m, m + 10):
        for l in range(mm, mm + 10):
            a[j][l] = 1
c = 0
for i in range(100):
    for j in range(100):
        if a[i][j] == 1:
            # 상
            if i == 0 or a[i-1][j] == 0:
                c += 1
            # 하
            if i == 99 or a[i+1][j] == 0:
                c += 1
            # 좌
            if j == 0 or a[i][j-1] == 0:
                c += 1
            # 우
            if j == 99 or a[i][j+1] == 0:
                c += 1
print(c)
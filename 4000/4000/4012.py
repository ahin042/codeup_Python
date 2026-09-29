n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    r = 1
    for j in range(n):
        if a[j] > a[i]:
            r += 1
    print(a[i], r)

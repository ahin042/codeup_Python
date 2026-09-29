n = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())  # a번째부터 b번째까지
t = sum(lst[a-1:b])
c = 0
for i in range(n):
    m = 0
    for j in range(i, n):
        m += lst[j]
        if m == t:
            c += 1
print(c)
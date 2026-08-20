a = int(input())
lst = []
for i in range(a):
    lst.append(list(map(int, input().split())))
c = 0
for i in range(6):
    m = [lst[j][i] for j in range(a)]
    c += max(m)
print(c)
a = int(input())
n = []
for i in range(a):
    lst = list(map(str, input().split(',')))
    n.append(len(lst[3:]))
c = 0
for i in n:
    c += i
print("%.2f" % (c / a))
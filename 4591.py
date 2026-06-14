a = []
for i in range(9) :
    j = int(input())
    a.append(j)
print(max(a))
print(a.index(max(a)) + 1)
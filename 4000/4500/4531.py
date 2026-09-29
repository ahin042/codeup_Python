n = 0 ; c = 0 ; a = []
for i in range(5) :
    n = int(input())
    a.append(n)
    c += n
a.sort()
print(c // 5)
print(a[2])
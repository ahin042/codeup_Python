n, *a = map(int, input().split())
a.sort(reverse = True)
m = 1 + n // 2
a[0], a[m-1] = a[m-1], a[0]
print(*a)
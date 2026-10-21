n = int(input())
a, b, c = map(int, input().split())
x = (n // 12) * a
y = (x // 8) * b
z = (y // 5) * c
print(z)
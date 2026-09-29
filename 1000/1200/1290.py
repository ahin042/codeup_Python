a = int(input())
r = a ; c = 0
for i in range(1, a):
    if a % i == 0:
        c += 1
print(c)
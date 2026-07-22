a = int(input())
c = 0
r = 0
for i in range(1, a + 1):
    c += i
    r = i
    if c >= a:
        break
print(r, c)
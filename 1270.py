n = int(input())
r = 0
for i in range(1, n + 1):
    if str(i)[-1] == '1':
        r += 1
print(r)
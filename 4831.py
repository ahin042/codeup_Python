a = int(input())
c = list(map(int, input().split()))
r = 0
for i in c:
    if i == a:
        r += 1
print(r)
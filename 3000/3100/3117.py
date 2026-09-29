k = int(input())
r = []
for i in range(k):
    n = int(input())
    if n == 0:
        r.pop()
    else:
        r.append(n)
print(sum(r))
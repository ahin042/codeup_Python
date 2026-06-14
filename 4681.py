n = list(map(int, input().split()))
c = 0
for i in n :
    c += i * i
print(c % 10)
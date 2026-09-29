n = list(map(str, input().split(".")))
for i in range(len(n) - 1) :
    print(n[i] + "-",end="")
print(n[-1])
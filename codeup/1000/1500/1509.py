n = []
for i in range(10):
    nn = list(map(int, input().split()))
    n.append(nn)
a = list(map(int, input().split()))
m = {}
for i in range(len(a)):
    if a[i] == 1:
        result = "safe"
        for j in range(len(n) - 1, -1, -1):
            if n[j][i] != 0:
                if n[j][i] > 0:
                    result = "crash"
                else:
                    result = "fall"
                break
        m[i + 1] = result
for i, j in m.items():
    print(i, j)
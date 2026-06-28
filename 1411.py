n = int(input())
a = []
for i in range(n - 1) :
    a.append(int(input()))
for i in range(1,n + 1) :
    if i not in a :
        print(i)
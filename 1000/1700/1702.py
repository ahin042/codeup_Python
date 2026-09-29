a = list(map(int, input().split()))
if (a[1] % 2 == 0):
    for j in range(2) :
        for i in a:
            print(i, end="")
        print(" ",end="")
else :
    for i in a:
        print(i, end="")
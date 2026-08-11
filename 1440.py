a = int(input())
lst = list(map(int,input().split()))
for i in range(a) :
    print(i + 1,end=":")
    for j in range(a) :
        if j != i:
            if lst[j] > lst[i]:
                print(" <", end="")
            elif lst[j] < lst[i]:
                print(" >", end="")
            else:
                print(" =", end="")
    print()
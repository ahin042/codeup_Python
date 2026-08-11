a, b = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in range(len(lst)):
    print(lst[i], end=" ")
    if (i + 1) % b == 0:
        print()
a = int(input())
lst = list(map(int, input().split()))
print(*lst)
for i in range(1,len(lst)):
    print(*lst[i:] + lst[:i])
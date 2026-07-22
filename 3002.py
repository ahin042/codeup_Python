a = int(input())
lst = list(map(int, input().split()))
i_map = {v: i + 1 for i, v in enumerate(lst)}
a = int(input())
find = list(map(int, input().split()))
for i in find:
    print(i_map.get(i, -1), end=" ")
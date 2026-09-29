a = int(input())
m = {}
for i in range(a) :
    lst = list(map(str, input().split(',')))
    m[lst[0]] = lst[3:]
find = input()
for i in m[find]:
    print(i)
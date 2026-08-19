a = int(input())
m = {}
for i in range(a) :
    lst = list(map(str, input().split(',')))
    m[lst[0]] = int(lst[2])
find = input()
print(m[find])
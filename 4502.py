n = int(input())
a = list(map(int, input().split()))
r = []
for i in range(n):
    r.insert(len(r) - a[i], i + 1) # 원하는 위치에 값을 끼워 넣는 함수
print(*r)
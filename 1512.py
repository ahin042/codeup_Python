n = int(input())
x, y = map(int, input().split())
x -= 1 ; y -= 1
m = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a = abs(i - x) # 절댓값 구해줌
        b = abs(j - y)
        m[i][j] = a + b + 1
for i in range(n):
    s = ''
    for j in range(n):
        s += str(m[i][j]) + ' '
    print(s)
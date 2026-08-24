a = []
for _ in range(10):
    a.append(list(map(int, input().split())))
def bfs(r, c):
    q = [(r, c)]
    a[r][c] = 0
    while q:
        r, c = q.pop()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < 10 and 0 <= nc < 10 and a[nr][nc] == 1:
                a[nr][nc] = 0
                q.append((nr, nc))
n = 0
for r in range(10):
    for c in range(10):
        if a[r][c] == 1:
            bfs(r, c)
            n += 1
print(n)
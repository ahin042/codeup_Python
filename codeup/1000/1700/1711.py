x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
if x1 <= x3 <= x2 and y1 <= y3 <= y2:
    print("충돌")
else:
    print("비충돌")
import math as m
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
d = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"{d:.2f}")
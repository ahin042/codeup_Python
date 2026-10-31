a, b = map(int, input().split())
r = int(input())
c, d = map(int, input().split())
distance = (c - a) ** 2 + (d - b) ** 2
if distance < r ** 2:
    print("in")
elif distance == r ** 2:
    print("on")
else:
    print("out")

t, a, b = map(int, input().split())
c = 0
time = t
while time < 90:
    c += 1
    time += 5
a += c
if a > b:
    print("win")
elif a == b:
    print("same")
else:
    print("lose")
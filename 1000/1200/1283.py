s = int(input())
d = int(input())
c = s
n = list(map(int, input().split()))
for i in n:
    c = c * (1 + i / 100)
r = round(c - s)
print(r)
if r > 0:
    print("good") 
elif r == 0:
    print("same")
else:
    print("bad")
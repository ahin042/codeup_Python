a,b = map(int,input().split())
n = [a + b, a - b, a * b]
n.sort()
print(n[1])
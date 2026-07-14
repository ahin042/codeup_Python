a,b = map(int,input().split())
n = max(a + b, a - b, a * b, a / b, a ** b, b + a, b - a, b * a, b / a, b ** a)
print("%.6f" % n)

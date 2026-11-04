a = int(input())
b = "ABCDEFGHIJKL"
c = (a - 2013) % 60
n = (c + 5) % 12
m = (c + 9) % 10
print(b[n] + str(m))
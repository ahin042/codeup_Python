n = input()
n = n[::-1]
n = int(n) * 2
if n >= 100 :
    n %= 100
print(n)
if n <= 50 :
    print("GOOD")
else :
    print("OH MY GOD")
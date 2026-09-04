n = int(input())
m = n ; r = ""
for a in range(2, m + 1):
    while m % a == 0:
        r += str(a) + " "
        m //= a
    if m == 1:
        break
print(r.strip())
n = int(input())
s = input()
r = ""
for i in range(len(s)):
    if i > 0 and (len(s) - i) % 3 == 0:
        r += ","
    r += s[i]

print(r)
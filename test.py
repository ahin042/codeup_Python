n = input()
if n[0] == ")" :
    n = n[1:]
a = 0 ; b = 0
for i in n :
    if i == "(" :
        a += 1
    elif i == ")" :
        b += 1
if a == b :
    print("true")
else :
    print("false")
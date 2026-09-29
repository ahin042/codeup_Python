n = int(input())
m = input()
m = m.lower()
a = 0 ; b = 0
for i in m :
    if i == 'a' :
        a += 1
    elif i == 'b' :
        b += 1
if a == b :
    print("Tie")
elif a > b :
    print("A")
else :
    print("B")
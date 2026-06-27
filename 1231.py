a = input()
m = ""
for i in a:
    if not i.isalnum():
        m = i
        break
lst = a.split(m)
c1 = int(lst[0])
c2 = int(lst[1])
if m == "+":
    print(c1 + c2)
elif m == "-":
    print(c1 - c2)
elif m == "*":
    print(c1 * c2)
elif m == "/":
    print("%.2f"%(c1 / c2))

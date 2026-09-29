a = input()
number = []
math = []
m = ""
for i in a :
    if i.isdigit() :
        m += i
    else :
        math.append(i)
        number.append(int(m))
        m = ""
math.pop()
for i in math :
    if i == "+" :
        number[0] += number[1]
        number.pop(1)
    elif i == "-" :
        number[0] -= number[1]
        number.pop(1)
    elif i == "*" :
        number[0] *= number[1]
        number.pop(1)
    elif i == "/" :
        number[0] //= number[1]
        number.pop(1)
print(*number)
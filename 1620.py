def number(a) :
    n = 0
    for i in a :
        n += int(i)
    if n < 10:
        return n
    else :
        return number(str(n))
a = str(input())
print(number(a))
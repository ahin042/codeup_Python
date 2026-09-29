def number(n) :
    if n > 0 :
        return "plus"
    elif n == 0:
        return "zero"
    else :
        return "minus"
n = int(input())
print(number(n))
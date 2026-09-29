def number(n) :
    if n == 0:
        return "zero"
    elif n > 0 :
        return "positive"
    else :
        return "negative"
n = int(input())
print(number(n))
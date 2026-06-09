def score(n) :
    if n >= 90 :
        return "A"
    elif n >= 80 :
        return "B"
    elif n >= 70 :
        return "C"
    elif n >= 60 :
        return "D"
    else :
        return "F"
n = int(input())
print(score(n))
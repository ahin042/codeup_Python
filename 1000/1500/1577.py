def change(n) :
    if n < 0 :
        n *= -1
        return n
    elif n == 0 :
        return 0
    else :
        return n
n = int(input())
print(change(n))
def number(n) :
    for i in range(1, n + 1):
        if i * i > n:
            return i - 1
        elif i * i == n:
            return i

num = int(input())
if num == 0 :
    print(0)
else :
    print(number(num))
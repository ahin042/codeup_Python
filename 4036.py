a1 = int(input())
a2 = int(input())
for i in range(1,a1) :
    if i - (a1 - i) == a2 :
        print(i)
        print(a1 - i)
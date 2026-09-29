n = int(input())
if n <= 500 :
    print(n * 70 // 100)
elif n <= 1500 :
    print(350 + (n - 500) * 40 // 100)
elif n <= 4500 :
    print(750 + (n - 1500) * 15 // 100)
elif n <= 10000 :
    print(1200 + (n - 4500) * 5 // 100)
else :
    print(1475 + (n - 10000) * 2 // 100)
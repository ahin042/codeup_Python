a = list(map(int, input().split()))
if a[0] == a[1] and a[1] == a[2] :
    print("정삼각형")
elif (a[0] == a[1] or a[1] == a[2] or a[2] == a[0]) and a[0] + a[1] > a[2]:
    print("이등변삼각형")
elif a[0] ** 2 + a[1] ** 2  == a[2] ** 2 and a[0] + a[1] > a[2]:
    print("직각삼각형")
elif a[0] + a[1] > a[2] and len(a) == 3 :
    print("삼각형")
else :
    print("삼각형아님")
y, m = map(int, input().split())
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if m == 2:
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print(29)
    else:
        print(28)
else:
    print(lst[m - 1])
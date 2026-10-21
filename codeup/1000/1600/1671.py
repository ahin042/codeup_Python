a, b = map(int, input().split())
if a == b:
    print("tie")
elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
    print("win")
else:
    print("lose")
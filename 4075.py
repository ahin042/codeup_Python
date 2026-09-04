n = input()
if n.lower() == n[::-1].lower():
    print("Yes")
    print(n[:(len(n)+1)//2])
else:
    print("No")
    print(n, end="")
    print(n[::-1])
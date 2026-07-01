n = input()
for i in range(len(n)) :
    print("+-",end="")
print("+")
for i in n :
    print("|" + i,end="")
print("|")
for i in range(len(n)) :
    print("+-",end="")
print("+")

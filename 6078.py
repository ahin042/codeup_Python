n = 'a' ; m = []
while n != 'q' :
    n = input()
    m.append(n)
    if n == 'q' :
        break
for i in m :
    print(i)
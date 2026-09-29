a,b = map(int,input().split())
c = 0
for i in range(a, b + 1) :
    if "1" in str(i) :
        for j in str(i) :
            if j == "1" :
                c += 1
print(c)
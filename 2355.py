a,b = map(int, input().split())
for i in range(1,a + 1) :
    if i % 2 == 0:
        print(" ",end=" ")
        for j in range(b - 1) :
            print("SFPC",end=" ")
    else :
        for j in range(b) :
            print("SFPC",end=" ")
    print("")
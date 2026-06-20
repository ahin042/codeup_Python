def m(a,b) :
    try :
        return a.index(b) + 1
    except ValueError :
        return -1
n1 = int(input())
n2 = list(map(int,input().split()))
n3 = int(input())
print(m(n2,n3))
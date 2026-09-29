def m(b,c,d) :
    n = b[c - 1 : d]
    r = max(n)
    return b.index(r) + 1


n1 = int(input())
n2 = list(map(int,input().split()))
n3,n4 = map(int,input().split())
print(m(n2,n3,n4))

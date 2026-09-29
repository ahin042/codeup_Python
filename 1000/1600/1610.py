def sub(a,b,c) :
    return a[b : b + c]
a = input()
b,c = map(int,input().split())
print(sub(a,b,c))
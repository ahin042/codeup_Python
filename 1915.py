def p(i,j,n) :
     if n == 1:
         return i
     return p(j, i + j, n - 1)
n = int(input())
print(p(1,1,n))
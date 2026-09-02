a = int(input())
n = list(map(int,input().split()))
a = int(input())
m = list(map(int,input().split()))
c = []
for i in m :
	if i in n :
		c.append(1)
	else :
		c.append(0)
print(*c)
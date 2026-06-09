def number(n):
	i = 0
	for j in range(1, n + 1):
		i += j
	return i
n = int(input())
print(number(n))
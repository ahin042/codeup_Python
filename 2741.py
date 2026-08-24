a = input()
m = input()
lst = {}
for i, j in enumerate(a):
    lst[j] = chr(ord('a') + i)
r = ''.join(lst[i] for i in m)
print(r)